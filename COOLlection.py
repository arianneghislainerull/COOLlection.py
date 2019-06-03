#COOLlection.py

import time

print ("Welcome to COOLlection!")#prints the string/greeting
time.sleep(1)#Buffers time
usern=input("What is your username? ")#prints the string/greeting
time.sleep(1)#Buffers time
print ("Hi",usern,", your fate is within your hands!")#prints the string/greeting
time.sleep(1)#Buffers time

print ("Foreword:\n The app can only be used by 10 years old and up.\n")#prints the string/greeting
age=input("What is your REAL age? ")#gets the input/age
#converts the input to integer
age=int(age)
if (age>9):#if age is more than 9, this would be the output
    print("You are more than 9 years old, hence you can use the app!\n")
    apps=input("Press the number of the mini-app that you want to use.\n COOLlection offers three apps.\n 1: HST Calculator \n 2: Space Invaders\n 3: Memory Tiles\n 4: Morse Code Translator\n")
    time.sleep(1)

    if apps=="1":
        print ("Great choice! You picked to use the HST Calculator!")

        print ('CANADIAN HST CALCULATOR')
        time.sleep(1)
        print ('HST is the Harmonized Sales Tax that is charged on specific items to support the federal and provincial government.\n')
        time.sleep(1)

        #OPTIONS for PROVINCES
        provinces=input("What province are you located in?\n Press the numbers\n 1: New Brunswick\n 2: Newfoundland and Labrador \n 3: Nova Scotia\n 4: Ontario\n 5: Prince Edward Island\n ")
        if provinces=='1':
            print("You have chosen that you are located in New Brunswick")
            
            #the command offers the options #Get the input from the user
            options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
            if options=='1':
                #1: price excluding HST
                print("You have chosen to calculate the price excluding HST ")
                print("FORMULA:\n p_w_hst - HST = price excluding HST ")
                #Get input from the user
                p_w_hst=input("Enter the price with the HST ")
                #Convert the string input to float
                p_w_hst=float(p_w_hst)
                #Get input from the user
                hst=input("Enter the HST ")
                #Convert the string input to float
                hst=float(hst)
                #Shows the input from the user
                print('Price with HST is:',p_w_hst,', HST is:',hst)
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                price_excluding_hst=(p_w_hst - hst)
                #Print the output
                print('The price excluding HST is', price_excluding_hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='2':
                #2: HST only
                print("You have chosen to calculate HST only")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
                #Get input from the user
                p_no_hst = input("Enter the price without HST ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst=(p_no_hst * 0.15)
                #Print the output
                print('The HST is', hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='3':
                #3: Federal part
                print("You have chosen to calculate the federal part")
                print("FORMULA:\n HST * federal part (5%/0.05)")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the federal part is 5% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                federal=(hst * 0.05)
                #Print the output
                print('The federal part is', federal)
                print('Thank you for using the HST Calculator!')
                
            if options=='4':
                #4: Provincial part
                print("You have chosen to calculate the provincial part")
                print("FORMULA:\n HST * provincial part")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the provincial part is 10% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                provincial=(hst * 0.1)
                #Print the output
                print('The provincial part is', provincial)
                print('Thank you for using the HST Calculator!')
                
            if options=='5':
                #5: Price with HST
                print("You have chosen to calculate the price including HST")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
                #Get input from the user
                p_no_hst = input ("Enter the price without HST  ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print("The price without HST is", p_no_hst,", the HST is 15%")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst = (p_no_hst * 0.15)
                p_w_hst = (hst + p_no_hst)
                #Print the output
                print('The price with HST is', p_w_hst)
                print('Thank you for using the HST Calculator!')
                
        if provinces=='2':
            print("You have chosen that you are located in Newfoundland and Labrador")
            
            #the command offers the options #Get the input from the user
            options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
            if options=='1':
                #1: price excluding HST
                print("You have chosen to calculate the price excluding HST ")
                print("FORMULA:\n p_w_hst - HST = price excluding HST ")
                #Get input from the user
                p_w_hst=input("Enter the price with the HST ")
                #Convert the string input to float
                p_w_hst=float(p_w_hst)
                #Get input from the user
                hst=input("Enter the HST ")
                #Convert the string input to float
                hst=float(hst)
                #Shows the input from the user
                print('Price with HST is:',p_w_hst,', HST is:',hst)
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                price_excluding_hst=(p_w_hst - hst)
                #Print the output
                print('The price excluding HST is', price_excluding_hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='2':
                #2: HST only
                print("You have chosen to calculate HST only")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
                #Get input from the user
                p_no_hst = input("Enter the price without HST ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst=(p_no_hst * 0.15)
                #Print the output
                print('The HST is', hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='3':
                #3: Federal part
                print("You have chosen to calculate the federal part")
                print("FORMULA:\n HST * federal part (5%/0.05)")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the federal part is 5% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                federal=(hst * 0.05)
                #Print the output
                print('The federal part is', federal)
                print('Thank you for using the HST Calculator!')
                
            if options=='4':
                #4: Provincial part
                print("You have chosen to calculate the provincial part")
                print("FORMULA:\n HST * provincial part")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the provincial part is 10% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                provincial=(hst * 0.1)
                #Print the output
                print('The provincial part is', provincial)
                print('Thank you for using the HST Calculator!')
                
            if options=='5':
                #5: Price with HST
                print("You have chosen to calculate the price including HST")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
                #Get input from the user
                p_no_hst = input ("Enter the price without HST  ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print("The price without HST is", p_no_hst,", the HST is 15%")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst = (p_no_hst * 0.15)
                p_w_hst = (hst + p_no_hst)
                #Print the output
                print('The price with HST is', p_w_hst)
                print('Thank you for using the HST Calculator!')
                
        if provinces=='3':
            print("You have chosen that you are located in Nova Scotia")

            #the command offers the options #Get the input from the user
            options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
            if options=='1':
                #1: price excluding HST
                print("You have chosen to calculate the price excluding HST ")
                print("FORMULA:\n p_w_hst - HST = price excluding HST ")
                #Get input from the user
                p_w_hst=input("Enter the price with the HST ")
                #Convert the string input to float
                p_w_hst=float(p_w_hst)
                #Get input from the user
                hst=input("Enter the HST ")
                #Convert the string input to float
                hst=float(hst)
                #Shows the input from the user
                print('Price with HST is:',p_w_hst,', HST is:',hst)
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                price_excluding_hst=(p_w_hst - hst)
                #Print the output
                print('The price excluding HST is', price_excluding_hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='2':
                #2: HST only
                print("You have chosen to calculate HST only")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
                #Get input from the user
                p_no_hst = input("Enter the price without HST ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst=(p_no_hst * 0.15)
                #Print the output
                print('The HST is', hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='3':
                #3: Federal part
                print("You have chosen to calculate the federal part")
                print("FORMULA:\n HST * federal part (5%/0.05)")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the federal part is 5% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                federal=(hst * 0.05)
                #Print the output
                print('The federal part is', federal)
                print('Thank you for using the HST Calculator!')
                
            if options=='4':
                #4: Provincial part
                print("You have chosen to calculate the provincial part")
                print("FORMULA:\n HST * provincial part")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the provincial part is 10% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                provincial=(hst * 0.1)
                #Print the output
                print('The provincial part is', provincial)
                print('Thank you for using the HST Calculator!')
                
            if options=='5':
                #5: Price with HST
                print("You have chosen to calculate the price including HST")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
                #Get input from the user
                p_no_hst = input ("Enter the price without HST  ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print("The price without HST is", p_no_hst,", the HST is 15%")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst = (p_no_hst * 0.15)
                p_w_hst = (hst + p_no_hst)
                #Print the output
                print('The price with HST is', p_w_hst)
                print('Thank you for using the HST Calculator!')
                
        if provinces=='4':
            print("You have chosen that you are located in Ontario")

            #the command offers the options #Get the input from the user
            options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
            if options=='1':
                #1: price excluding HST
                print("You have chosen to calculate the price excluding HST ")
                print("FORMULA:\n p_w_hst - HST = price excluding HST ")
                #Get input from the user
                p_w_hst=input("Enter the price with the HST ")
                #Convert the string input to float
                p_w_hst=float(p_w_hst)
                #Get input from the user
                hst=input("Enter the HST ")
                #Convert the string input to float
                hst=float(hst)
                #Shows the input from the user
                print('Price with HST is:',p_w_hst,', HST is:',hst)
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                price_excluding_hst=(p_w_hst - hst)
                #Print the output
                print('The price excluding HST is', price_excluding_hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='2':
                #2: HST only
                print("You have chosen to calculate HST only")
                print("FORMULA:\n p_no_hst * 13% or 0.13 = HST")
                #Get input from the user
                p_no_hst = input("Enter the price without HST ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst=(p_no_hst * 0.13)
                #Print the output
                print('The HST is', hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='3':
                #3: Federal part
                print("You have chosen to calculate the federal part")
                print("FORMULA:\n HST * federal part (5%/0.05)")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the federal part is 5% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                federal=(hst * 0.05)
                #Print the output
                print('The federal part is', federal)
                print('Thank you for using the HST Calculator!')
                
            if options=='4':
                #4: Provincial part
                print("You have chosen to calculate the provincial part")
                print("FORMULA:\n HST * provincial part")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the provincial part is 8% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                provincial=(hst * 0.08)
                #Print the output
                print('The provincial part is', provincial)
                print('Thank you for using the HST Calculator!')
                
            if options=='5':
                #5: Price with HST
                print("You have chosen to calculate the price including HST")
                print("FORMULA:\n p_no_hst * 13% or 0.13 = HST\n HST + p_no_hst = price with HST")
                #Get input from the user
                p_no_hst = input ("Enter the price without HST  ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print("The price without HST is", p_no_hst,", the HST is 15%")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst = (p_no_hst * 0.13)
                p_w_hst = (hst + p_no_hst)
                #Print the output
                print('The price with HST is', p_w_hst)
                print('Thank you for using the HST Calculator!')
                
        if provinces=='5':
            print("You have chosen that you are located in Prince Edward Island")
            #the command offers the options #Get the input from the user
            options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
            if options=='1':
                #1: price excluding HST
                print("You have chosen to calculate the price excluding HST ")
                print("FORMULA:\n p_w_hst - HST = price excluding HST ")
                #Get input from the user
                p_w_hst=input("Enter the price with the HST ")
                #Convert the string input to float
                p_w_hst=float(p_w_hst)
                #Get input from the user
                hst=input("Enter the HST ")
                #Convert the string input to float
                hst=float(hst)
                #Shows the input from the user
                print('Price with HST is:',p_w_hst,', HST is:',hst)
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                price_excluding_hst=(p_w_hst - hst)
                #Print the output
                print('The price excluding HST is', price_excluding_hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='2':
                #2: HST only
                print("You have chosen to calculate HST only")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
                #Get input from the user
                p_no_hst = input("Enter the price without HST ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst=(p_no_hst * 0.15)
                #Print the output
                print('The HST is', hst)
                print('Thank you for using the HST Calculator!')
                
            if options=='3':
                #3: Federal part
                print("You have chosen to calculate the federal part")
                print("FORMULA:\n HST * federal part (5%/0.05)")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the federal part is 5% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                federal=(hst * 0.05)
                #Print the output
                print('The federal part is', federal)
                print('Thank you for using the HST Calculator!')
                
            if options=='4':
                #4: Provincial part
                print("You have chosen to calculate the provincial part")
                print("FORMULA:\n HST * provincial part")
                #Get input from the user
                hst = input ("Enter the HST ")
                #Convert the string input to float
                hst = float (hst)
                #Shows the input from the user
                print("The HST is",hst,", the provincial part is 10% of HST")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                provincial=(hst * 0.1)
                #Print the output
                print('The provincial part is', provincial)
                print('Thank you for using the HST Calculator!')
                
            if options=='5':
                #5: Price with HST
                print("You have chosen to calculate the price including HST")
                print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
                #Get input from the user
                p_no_hst = input ("Enter the price without HST  ")
                #Convert the string input to float
                p_no_hst = float (p_no_hst)
                #Shows the input from the user
                print("The price without HST is", p_no_hst,", the HST is 15%")
                print("Loading.....")
                #Buffer time
                time.sleep(5)
                #Use the algorithm to calculate
                hst = (p_no_hst * 0.15)
                p_w_hst = (hst + p_no_hst)
                #Print the output
                print('The price with HST is', p_w_hst)
                print('Thank you for using the HST Calculator!')


        
    if apps=="2":
        print ("Great choice! You picked to use the Space Invaders!")

        #Space Invaders

        import turtle
        import os
        import math
        import random
        import winsound
        import sys
        import time

        #Uses the sys module and time
        from time import sleep
        for i in range(101):
            sys.stdout.write('\r')
            sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
            sys.stdout.flush()
            #It takes 3 milliseconds to load
            sleep(0.03)
            
        ###Set up the screen###
        mainscreen = turtle.Screen()
        #Screen Attributes#
        mainscreen.bgcolor ("black")
        mainscreen.title("Space Invaders")
        #files/graphics must be on the same folder
        mainscreen.bgpic("space_invaders_background.gif")

        #Register the shapes
        turtle.register_shape("invader.gif")
        turtle.register_shape("player.gif")

        ###Draw border###
        border_pen = turtle.Turtle()
        #Border Attributes#
        border_pen.speed(0)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300,-300)
        border_pen.pendown()
        border_pen.pensize(3)
        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)
        #Hides the turtle#
        border_pen.hideturtle()

        #SET THE SCORE to 0
        score = 0

        #Draw the score
        score_pen = turtle.Turtle()
        #Score's attributes
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()#not want to draw
        score_pen.setposition(-290, 280)
        scorestring = "Score: %s" %score
        score_pen.write(scorestring, False, align="left", font=("Arial", 13, "normal"))
        score_pen.hideturtle()

        ###Create the player turtle###
        player = turtle.Turtle()
        #Turtle Attributes#
        player.color("blue")
        player.shape("player.gif")
        player.penup()
        player.speed(0)
        player.setposition(0, -250)
        player.setheading(90)

        #Player moves 15 pixels each
        playerspeed = 15

        #Choose a number of enemies
        number_of_enemies = 5
        #Create an empty list of enemies
        enemies = []

        #Add enemies to the list
        for i in range(number_of_enemies):
        #Create the enemy/invader using a turtle
            enemies.append(turtle.Turtle())
        #Enemy attributes
        for enemy in enemies:
            enemy.color("red")
            enemy.shape("invader.gif")
            enemy.penup()
            enemy.speed(0)

            #x-coordinate(x)
            x = random.randint(-200, 200)
            #y-coordinate(y)
            y = random.randint(100, 250)
            #(x,y) coordinates
            enemy.setposition(x, y)

        #enemy is slower than player
        enemyspeed = 2

        #Create the player's bullet
        bullet = turtle.Turtle()
        #Bullet Attributes
        bullet.color ("yellow")
        bullet.shape ("circle")
        bullet.penup()
        bullet.speed(0)
        bullet.setheading(90)
        bullet.shapesize(0.6,0.6)
        bullet.hideturtle()

        bulletspeed = 20

        #Define bullet state
        #Ready - ready to fire
        #fire - bullet is firing
        bulletstate = "ready"

        #Move the player left and right
        #for left
        def move_left():
            #X-coordinate
            #Game starts with 0
            x = player.xcor()
            #Takes the current value of x, subtracts player speed and assign that to X
            x -= playerspeed
            ##BOUNDARY CHECKING##
            #Blocks the player from moving below -280
            if x < -280:
                x = -280
            player.setx(x)

        #for right
        def move_right():
            #set x
            x = player.xcor()
            #Takes the current value of x, subtracts player speed and assign that to X
            x += playerspeed
            ##BOUNDARY CHECKING##
            #Blocks the player from moving more than 280
            if x > 280:
                x = 280
            player.setx(x)

        #firing the bullet
        def fire_bullet():
            #Declare bulletstate as if it needs to be changed
            global bulletstate
            if bulletstate == "ready":
                #This is for the laser sound#laser sounds plays when the bullet is in ready state
                winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
                bulletstate = "fire"
                #Move the bullet to above the player
                x = player.xcor()
                y = player.ycor() + 10
                bullet.setposition(x, y)
                bullet.showturtle()

        #defining the collision
        def isCollision(t1, t2):
            distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
            if distance <15:
                return True
            else:
                return False

        #Create keyboard bindings
        turtle.listen()#follow the keyboard bindins
        turtle.onkey(move_left, "Left")#left arrow
        turtle.onkey(move_right, "Right")#right arrow
        turtle.onkey(fire_bullet, "space")#space to fire bullet

        #Main Game Loop
        while True:

            for enemy in enemies:
                #Move the enemy
                x = enemy.xcor()
                x += enemyspeed
                enemy.setx(x)

                #Move the enemy back and down
                #Right side
                if enemy.xcor() > 280:
                    #Move all enemies down
                    for e in enemies:
                        #y coordinate
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                    #Change enemy direction
                    enemyspeed *= -1
                    
                #Left side
                if enemy.xcor() < -280:
                    #Move all enemies down
                    for e in enemies:
                        #y coordinate
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                    #Change enemy direction
                    enemyspeed *= -1
                    
                #Check for a collision between the bullet and the enemy
                if isCollision(bullet, enemy):
                    #This is for the explosion sound
                    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                    #Reset the bullet
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.setposition (0, -400)

                    #Reset the enemy
                    #x-coordinate(x)
                    x = random.randint(-200, 200)
                    #y-coordinate(y)
                    y = random.randint(100, 250)
                    #(x,y) coordinates
                    enemy.setposition(x, y)

                    #Update the score
                    score += 10
                    scorestring = "Score: %s" %score
                    #clears the score
                    score_pen.clear()
                    score_pen.write(scorestring, False, align="left", font=("Arial", 13, "normal"))

                #Check for a collision between the player and the enemy
                if isCollision(player, enemy):
                    #This is for the explosion sound
                    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                    player.hideturtle()
                    enemy.hideturtle()

                    #Draw the Game over
                    gameover_pen = turtle.Turtle()
                    #Game Over's attributes
                    gameover_pen.speed(0)
                    gameover_pen.color("white")
                    gameover_pen.penup()#not want to draw
                    gameover_pen.setposition(10, 0)
                    gameoverstring = "Game Over!" 
                    gameover_pen.write(gameoverstring, False, align="center",font=("Arial", 60, "bold"))
                    gameover_pen.hideturtle()
                    
                    gameoverstring = "Game Over!" 
                    print ("Game Over")
                    break
                
            #Move the bullet
            #state controls the bullet condition
            if bulletstate == "fire":
                y = bullet.ycor()
                y += bulletspeed
                bullet.sety(y)

            #Check to see if the bullet is going to the top
            if bullet.ycor() > 275:
                bullet.hideturtle()
                bulletstate = "ready"
                
        delay = raw_input("Press enter to finish")
        
    if apps=="3":
        print("Great choice! You picked to use the Memory Tile Game!")
        
        #Memory tiles

        #import
        import random
        import time
        score = 0
        #prints the instructions
        print ('This is the memory tile game.\n The goal is to match two pairs from the tile of the same letter.\n The asterisks represent the place of the tile.\n The rows are the x-coordinates, while the columns are the y-coordinates.\n Type (x,y) coordinates of the tiles to match them with another pair.\n')
        time.sleep(2)
        
        #Variables with their pairs
        answer = list('AABBCCDDEEFFGGHH')
        #Shuffles and randomizes the variables
        random.shuffle(answer)
        answer = [answer[:4],
                 answer[4:8],
                 answer[8:12],
                 answer[12::]]
        
        #four rows of asterisks
        board = [list('*'*4)for i in range(4)]
        
        #function to choose
        #Allows the player to choose
        def choose():
            a,b = map (int, input('? '))
            show_board((a,b))
            x,y = map (int, input('? '))
            
            #Shows the board with the pattern
            show_board ((a,b),(x,y))
            time.sleep(2)#2-second delay
            
            #Waits for two seconds to figure out, if it is a match or not
            if answer[a][b] == answer[x][y]:
                #correct pattern - result
                tscore = score + 1
                print('Great Job! It is a match!')
                print('You have', tscore ,'point/s')
                board[a][b] = answer[a][b]
                board[x][y] = answer[x][y]
                
            else:
                #incorrect pattern - result
                print('Sorry, not a match.')
                
            #figures out if there are any asterisks in any row
            if any('*' in row for row in board):
                #keeps going, even if there are no matches
                return True
        
        #Function to choose the necessary tiles
        def show_board(*tiles):
            for row in range(len(answer[0])):
                for column in range(len(answer[0])):
                    if (row, column) in tiles:
                        print(answer[row][column].lower(), end='', flush=True)
                    else:
                        print(board[row][column], end='', flush=True)
                print()
                    
        #Starts by showing the board
        show_board()
        
        #defines t
        #uses monotonic method of counting the time
        t = time.monotonic()
        
        while choose():
            pass
        
        #prints the time
        print('Completed!\n Time:', time.monotonic()-t)

    if apps=="4":
        print ("Great choice! You picked to use the Morse Code Translator!")
        
        #Morse Code Translator
        
        #Greeting
        print('This is a Morse Code Translator.')
        #Gets the input
        choice = input('Press 1 to convert word text to morse code.\n Press 2 to convert morse code to word text.\n')
        
        if choice=="1":#if the input is 1
            #define to_morse_code
            def to_morse_code(text):
                #translation of word characters
                code = {'a':'.-', 'b':'-...', 
                        'c':'-.-.', 'd':'-..', 'e':'.', 
                        'f':'..-.','g':'--.', 'h':'....', 
                        'i':'..', 'j':'.---', 'k':'-.-', 
                        'l':'.-..', 'm':'--', 'n':'-.', 
                        'o':'---', 'p':'.--.', 'q':'--.-', 
                        'r':'.-.', 's':'...', 't':'-', 
                        'u':'..-', 'v':'...-', 'w':'.--', 
                        'x':'-..-', 'y':'-.--', 'z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-', ' ':' '}
                morse_code =""
                
                #translates each character into morse_code
                for x in text:
                    morse_code += code[x.lower()]
                #return command does not print the value
                return morse_code
            
            #Program asks for the user's input to be converted
            text = input("Enter NORMAL TEXT to convert to MORSE CODE: ")
            #Prints the output()
            print(to_morse_code(text))
            print('Thank you for using the program!')
        
        if choice=="2":#if the input is 2
            #define to_normal_text
            def to_normal_text(text):
                #translation of word characters
                alphabet = {'.-':'a', '-...':'b', 
                        '-.-.':'c', '-..':'d', '.':'e',
                        '..-.':'f', '--.':'g', '....':'h',
                        '..':'i', '.---':'j', '-.-':'k',
                        '.-..':'l', '--':'m', '-.':'n',
                        '---':'o', '.--.':'p', '--.-':'q',
                        '.-.':'r', '...':'s', '-':'t',
                        '..-':'u', '...-':'v', '.--':'w',
                        '-..-':'x', '-.--':'y', '--..':'z',
                        '.----':'1', '..---':'2', '...--':'3',
                        '....-':'4', '.....':'5', '-....':'6',
                        '--...':'7', '---..':'8', '----.':'9',
                        '-----':'0', '--..--':', ', '.-.-.-':'.',
                        '..--..':'?', '-..-.':'/', '-....-':'-',
                        '-.--.':'(', '-.--.-':')', ' ':' '}
                to_normal_text=""
                
                #translates each character into morse_code
                for x in text:
                    to_normal_text += alphabet[x.lower()]
                            
                return to_normal_text
            
            #Program asks for the user's input to be converted
            text = input("Enter MORSE CODE to convert to NORMAL TEXT: ")
            #Prints the output()
            print(to_normal_text(text))   
            print('Thank you for using the program!')
 

else:
    print("Sorry, you are not yet 10 years old.\n Therefore, you cannot use the app.\n")





