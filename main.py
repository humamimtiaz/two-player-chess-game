import pygame

pygame.init()
width = 1000
height = 900
screen = pygame.display.set_mode((width,height))
font = pygame.font.Font('freesansbold.ttf', 20) # fonts change
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
framepersec = 60
pygame.display.set_caption('Multiplayer Chess')

# creating a counter for checking the variables
count = 0
gameo = False
# setting up the game variables and the images
whitepieces=['rook', 'knight','bishop','king','queen','bishop','knight','rook','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

blackpieces=['rook', 'knight','bishop','king','queen','bishop','knight','rook','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

# locations of the pieces on the board
whitelocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
blacklocs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# list captured pieces
capturewhite = []
captureblack = []
turns = 0
win = ''
# 0,1,2,3 = white 0 no selection, 1 selection, black 2 no selection, 3 selection
# loop for the main game
selected = 100 # will store the index of the selected piece
validmoves = [] # a list to check the valid moves of the pieces

# loading the images
bqueen = pygame.image.load('assets/images/black queen.png')
bqueen = pygame.transform.scale(bqueen, (80, 80)) #for the piece on the board
bqueen_small = pygame.transform.scale(bqueen, (45, 45))  # for the piece that is captured
bking = pygame.image.load('assets/images/black king.png')
bking = pygame.transform.scale(bking, (80, 80))
bking_small = pygame.transform.scale(bking, (45, 45))
brook = pygame.image.load('assets/images/black rook.png')
brook = pygame.transform.scale(brook, (80, 80))
brook_small = pygame.transform.scale(brook, (45, 45))
bbishop = pygame.image.load('assets/images/black bishop.png')
bbishop = pygame.transform.scale(bbishop, (80, 80))
bbishop_small = pygame.transform.scale(bbishop, (45, 45))
bknight = pygame.image.load('assets/images/black knight.png')
bknight = pygame.transform.scale(bknight, (80, 80))
bknight_small = pygame.transform.scale(bknight, (45, 45))
bpawn = pygame.image.load('assets/images/black pawn.png')
bpawn = pygame.transform.scale(bpawn, (65, 65))
bpawn_small = pygame.transform.scale(bpawn, (45, 45))
wqueen = pygame.image.load('assets/images/white queen.png')
wqueen = pygame.transform.scale(wqueen, (80, 80))
wqueen_small = pygame.transform.scale(wqueen, (45, 45))
wking = pygame.image.load('assets/images/white king.png')
wking = pygame.transform.scale(wking, (80, 80))
wking_small = pygame.transform.scale(wking, (45, 45))
wrook = pygame.image.load('assets/images/white rook.png')
wrook = pygame.transform.scale(wrook, (80, 80))
wrook_small = pygame.transform.scale(wrook, (45, 45))
wbishop = pygame.image.load('assets/images/white bishop.png')
wbishop = pygame.transform.scale(wbishop, (80, 80))
wbishop_small = pygame.transform.scale(wbishop, (45, 45))
wknight = pygame.image.load('assets/images/white knight.png')
wknight = pygame.transform.scale(wknight, (80, 80))
wknight_small = pygame.transform.scale(wknight, (45, 45))
wpawn = pygame.image.load('assets/images/white pawn.png')
wpawn = pygame.transform.scale(wpawn, (65, 65))
wpawn_small = pygame.transform.scale(wpawn, (45, 45))
wimages = [wpawn, wqueen, wking, wknight, wrook, wbishop] #can use the list to draw the images on the screen
swhite_images = [wpawn_small, wqueen_small, wking_small, wknight_small, wrook_small, wbishop_small]
bimages = [bpawn, bqueen, bking, bknight, brook, bbishop]
sblack_images = [bpawn_small, bqueen_small, bking_small, bknight_small, brook_small, bbishop_small]
pieceslist = ['pawn','queen','king','knight','rook','bishop']

# drawing the chess board
def drawboard():
    # for the 8x8 board alternating colours so for 64/2 we use 32 for one color
    for i in range(32):
        column = i%4 #0,1,2,3
        row = i//4 #row will remain same until after 4
        # need to do this for every other row
        if row % 2 == 0:
            pygame.draw.rect(screen, 'white', [600 - (column*200), row*100, 100, 100])
        else:
            pygame.draw.rect(screen, 'white', [700 - (column*200), row*100, 100, 100])

        pygame.draw.rect(screen, 'dark gray', [0,800,width,100])
        statet = ["WHITE'S TURN - Select a piece", "WHITE'S TURN - Place the piece", "BLACK'S TURN - Select a piece", "BLACK'S TURN - Place the piece"]
        # to ensure the font is large and rendered correctly - and text colour
        screen.blit(big_font.render(statet[turns], True, 'black'), (20, 820))
        # draw lines to separate the boxes
        for i in range(9):
            pygame.draw.line(screen, 'red', (0,100*i), (800,100*i), 2)
            pygame.draw.line(screen, 'red', (100 * i,0), (100 * i,800), 2)

# draw piece
def drawpiece():
    for i in range(len(whitepieces)):
        index = pieceslist.index(whitepieces[i])

        if whitepieces[i] == 'pawn':
            screen.blit(wpawn, (whitelocs[i][0]*100+22, whitelocs[i][1]*100+30) ) # need to do separate for pawns cuz theres more than 1
        else:
            screen.blit(wimages[index], (whitelocs[i][0] * 100 + 10, whitelocs[i][1] * 100 + 10))

        # if a piece is selected
        if turns<2: # white players turn
            if selected==i:
                pygame.draw.rect(screen, 'blue', [whitelocs[i][0]*100+1, whitelocs[i][1]*100+1, 100, 100], 2)


    for i in range(len(blackpieces)):
        index = pieceslist.index(blackpieces[i])

        if blackpieces[i] == 'pawn':
            screen.blit(bpawn, (blacklocs[i][0]*100+22, blacklocs[i][1]*100+30) ) # need to do separate for pawns cuz theres more than 1
        else:
            screen.blit(bimages[index], (blacklocs[i][0] * 100 + 10, blacklocs[i][1] * 100 + 10))
        # if a piece is selected
        if turns<1: # black players turn
            if selected==i:
                pygame.draw.rect(screen, 'blue', [blacklocs[i][0]*100+1, blacklocs[i][1]*100+1, 100, 100], 2)

# checking options for the pieces - where they can be moved
def checkopt(pieces, locs, turn):
    movel = []
    movesall = []
    for i in range(len(pieces)):
        location = locs[i]
        pi = pieces[i]
        # to check what piece is selected and check its valid moves accordingly
        if pi == 'pawn':
            movel = cpawn(location, turn)
        elif pi == 'rook':
            movel = crook(location, turn)
        elif pi == 'knight':
            movel = cknight(location, turn)
        elif pi == 'bishop':
            movel = cbishop(location, turn)
        elif pi == 'queen':
            movel = cqueen(location, turn)
        elif pi == 'king':
            movel = cking(location, turn)


        movesall.append(movel)

    return movesall

def cpawn(location, turn):
    movel = []
    if turn == 'white':
        # to check if the spot below is not occupied so the pawn can move forward for 1 and 2 squares forward
        if (location[0], location[1]+1) not in whitelocs and (location[0], location[1]+1) not in blacklocs and location[1]<7:
            movel.append((location[0], location[1]+1))

        if (location[0], location[1]+2) not in whitelocs and (location[0], location[1]+2) not in blacklocs and location[1]==1:
            movel.append((location[0], location[1]+2))

        # checking for diagonal
        if (location[0]+1, location[1]+1) in blacklocs:
            movel.append((location[0]+1, location[1] + 1))

        if (location[0]-1, location[1]+1) in blacklocs:
            movel.append((location[0]-1, location[1] + 1))

    elif turn == 'black':
        # to check if the spot below is not occupied so the pawn can move forward for 1 and 2 squares forward
        if (location[0], location[1]-1) not in whitelocs and (location[0], location[1]-1) not in blacklocs and location[1]>0:
            movel.append((location[0], location[1]-1))

        if (location[0], location[1]-2) not in whitelocs and (location[0], location[1]-2) not in blacklocs and location[1]==6:
            movel.append((location[0], location[1]-2))

        # checking for diagonal
        if (location[0]+1, location[1]-1) in whitelocs:
            movel.append((location[0]+1, location[1] - 1))

        if (location[0]-1, location[1]-1) in whitelocs:
            movel.append((location[0]-1, location[1] - 1))
    return movel

def crook(location, turn):
    movel = []
    if turn == 'white':
        enemyl = blacklocs # the enemies list will be the locations of the black pieces - this tells it what to hit and what not to
        friendl = whitelocs
    else:
        enemyl = whitelocs
        friendl = blacklocs
    for i in range(4): # rook checks up, down, left, right so 4 indexes
        free = True # the path is empty
        ch = 1
        if i == 0: #up
            x=0
            y=1
        elif i == 1: #down
            x=0
            y=-1
        elif i == 2: #right
            x=1
            y=0
        elif i == 3: #left
            x=-1
            y=0
        while free: # if it is true the loop runs to find a path if the position is available or else it shows the path as false
            if (location[0]+(ch*x), location[1]+(ch*y)) not in friendl and 0<=location[0]+(ch*x)<=7 and 0<=location[1]+(ch*y)<=7:
                movel.append((location[0]+(ch*x), location[1]+(ch*y)))

                if (location[0]+(ch*x), location[1]+(ch*y)) in enemyl:
                    free = False
                ch = ch+1
            else:
                free = False

    return movel

def cbishop(location, turn):
    movel = []
    if turn == 'white':
        enemyl = blacklocs
        friendl = whitelocs
    else:
        enemyl = whitelocs
        friendl = blacklocs
    for i in range(4): # rook checks up right and left, down right and left so 4 indexes
        free = True # the path is empty
        ch = 1
        if i == 0: #up
            x=1
            y=-1
        elif i == 1: #down
            x=-1
            y=-1
        elif i == 2: #right
            x=1
            y=1
        elif i == 3: #left
            x=-1
            y=1
        while free:
            if (location[0]+(ch*x), location[1]+(ch*y)) not in friendl and 0<=location[0]+(ch*x)<=7 and 0<=location[1]+(ch*y)<=7:
                movel.append((location[0]+(ch*x), location[1]+(ch*y)))

                if (location[0]+(ch*x), location[1]+(ch*y)) in enemyl:
                    free = False
                ch = ch+1
            else:
                free = False
    return movel

def cknight(location, turn): # 8 checking squares - 2 in each direction then 1 in different
    movel = []
    if turn == 'white':
        enemyl = blacklocs
        friendl = whitelocs
    else:
        enemyl = whitelocs
        friendl = blacklocs
    #hardcoding the spaces it can move
    spacem = [(1,2), (1,-2), (2,1), (2, -1), (-1,2), (-1, -2), (-2, 1), (-2,-1)]
    for i in range(8):
        spacet = (location[0]+spacem[i][0], location[1]+spacem[i][1])
        if spacet not in friendl and 0<=spacet[0]<=7 and 0<=spacet[1]<=7: # checking to see if the square exists and it is an enemy not a friend
            movel.append(spacet)

    return movel

def cqueen(location, turn):
    movel = cbishop(location, turn) #combine bishop and rook since queen uses both those moves
    secl = crook(location, turn)
    for i in range(len(secl)):
        movel.append(secl[i])

    return movel

def cking(location, turn): # go one square in any direction
    movel = []
    if turn == 'white':
        enemyl = blacklocs
        friendl = whitelocs
    else:
        enemyl = whitelocs
        friendl = blacklocs

    spacem = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        spacet = (location[0] + spacem[i][0], location[1] + spacem[i][1])
        if spacet not in friendl and 0 <= spacet[0] <= 7 and 0 <= spacet[1] <= 7:  # checking to see if the square exists and it is an enemy not a friend
            movel.append(spacet)

    return movel

# checking valid moves for selected piece
def checkvm():
    if turns < 2:
        optionl = whiteop
    else:
        optionl = blackop
    validop = optionl[selected]
    return validop

# valid moves drawn on the screen - moving images
def drawv(vmove):
    cl = 'blue'
    for i in range(len(vmove)):
        pygame.draw.circle(screen, cl, (vmove[i][0]*100+50, vmove[i][1]*100+50),5)

# if a king is in check it will draw a square that will flash to warn the player that their king is in danger
def checkmate():

    if turns < 2:
        if 'king' in whitepieces:
            kingi = whitepieces.index('king')
            kingloc = whitelocs[kingi]
            for i in range(len(blackop)):
                if kingloc in blackop[i]:
                    if count < 15:
                        pygame.draw.rect(screen, 'purple', [whitelocs[kingi][0]*100+1, whitelocs[kingi][1]*100+1,100,100], 5 )
    else:
        if 'king' in blackpieces:
            kingi = blackpieces.index('king')
            kingloc = blacklocs[kingi]
            for i in range(len(whiteop)):
                if kingloc in whiteop[i]:
                    if count < 15:
                        pygame.draw.rect(screen, 'purple',
                                         [blacklocs[kingi][0] * 100 + 1, blacklocs[kingi][1] * 100 + 1, 100, 100], 5)
# for the captured pieces drawing
def drawcatch():
    for i in range(len(capturewhite)):
        capp = capturewhite[i]
        inn = pieceslist.index(capp)
        screen.blit(sblack_images[inn], (825, 5+50*i))

    for i in range(len(captureblack)):
        capp = captureblack[i]
        inn = pieceslist.index(capp)
        screen.blit(swhite_images[inn], (925, 5+50*i))

def dgameo():
    pygame.draw.rect(screen, 'black', [200,200,400,50])
    screen.blit(font.render(f'{win} is the winner!', True, 'red'),(210,210))
    screen.blit(font.render(f'TO RESTART, CLICK ENTER!', True, 'white'), (210, 240))

# loop the main game
blackop = checkopt(blackpieces, blacklocs, 'black') # pass parameters to check options for each piece
whiteop = checkopt(whitepieces, whitelocs, 'white')
play = True
while play:
    timer.tick(framepersec)
    if count < 30:
         count = count + 1
    else:
        count = 0
    screen.fill('black')
    drawboard()
    drawpiece()
    drawcatch()
    checkmate()
    if selected != 100:
        validmoves = checkvm()
        drawv(validmoves)

    # for event handling - what is pressed on screen/keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks if the screen close [x] button was pressed
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameo:
            xcordinate = event.pos[0]//100
            ycordinate = event.pos[1] // 100
            clickcordinate = (xcordinate,ycordinate)
            # event.pos tels us the x and y coordinate of the mouse click that just happened

            # for checking white and black's turn and allowing clicks accordingly
            if turns < 2:
                if clickcordinate in whitelocs: # if the click is in any of the white chess pieces locations
                    selected = whitelocs.index(clickcordinate)
                    if turns == 0:  # nothing selected
                        turns = 1 # something selected

                if clickcordinate in validmoves and selected != 100: # if the selected piece (in the coordinate) is a valid move it will allow for it to happen
                    whitelocs[selected] = clickcordinate
                    if clickcordinate in blacklocs:
                        blackppiece = blacklocs.index(clickcordinate) #check index of the piece taken
                        capturewhite.append(blackpieces[blackppiece]) # append that in the captured list of the white pieces
                        if blackpieces[blackppiece]=='king':
                            win = 'white'
                        blackpieces.pop(blackppiece) # pop it from the black pieces
                        blacklocs.pop(blackppiece)

                    #checking the options for the moved pieces
                    blackop = checkopt(blackpieces, blacklocs, 'black') # pass parameters to check options for each piece
                    whiteop = checkopt(whitepieces, whitelocs, 'white')
                    # change everything back so the black can make the move next
                    turns = 2
                    selected = 100
                    validmoves = []

            # for checking the blacks turn - code is similar to whites
            if turns > 1:
                if clickcordinate in blacklocs: # if the click is in any of the white chess pieces locations
                    selected = blacklocs.index(clickcordinate)
                    if turns == 2:  # nothing selected
                        turns = 3 # something selected

                if clickcordinate in validmoves and selected != 100: # if the selected piece (in the coordinate) is a valid move it will allow for it to happen
                    blacklocs[selected] = clickcordinate
                    if clickcordinate in whitelocs:
                        whiteppiece = whitelocs.index(clickcordinate) #check index of the piece taken
                        captureblack.append(whitepieces[whiteppiece]) # append that in the captured list of the white pieces
                        if whitepieces[whiteppiece]=='king':
                            win = 'black'
                        whitepieces.pop(whiteppiece) # pop it from the black pieces
                        whitelocs.pop(whiteppiece)

                    #checking the options for the moved pieces
                    blackop = checkopt(blackpieces, blacklocs, 'black') # pass parameters to check options for each piece
                    whiteop = checkopt(whitepieces, whitelocs, 'white')
                    # change everything back so the black can make the move next
                    turns = 0
                    selected = 100
                    validmoves = []

        if event.type == pygame.KEYDOWN and gameo: # for starting a new game and clicking enter
            if event.key == pygame.K_RETURN:
                gameo = False
                win = ''
                whitepieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                blackpieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                               'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                whitelocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1),
                             (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                blacklocs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6),
                             (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                blackop = checkopt(blackpieces, blacklocs, 'black')
                whiteop = checkopt(whitepieces, whitelocs, 'white')
                capturewhite = []
                captureblack = []
                turns = 0
                selected = 100
                validmoves = []


    if win != '':
        gameo = True
        dgameo()


    pygame.display.flip()
pygame.quit()