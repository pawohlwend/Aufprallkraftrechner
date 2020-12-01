
def setup():                        #Initialisierung
    
    #globale Variablen
    global i
    i = "IMPACT FORCE OF A FALLING CLIMBER" 
    startMenu()
    size (800,600)                  #Fenstergrösse 

def startMenu (): 
    background (0)                  #Hintergrundfarbe
    

    fill(255, 255, 255)             #Textfarbe und Textgrösse
    textSize(20)       
    textAlign(CENTER)  
    text(i, 400,200)    
    text("START", 400, 330)                     
    noFill() 
    stroke (200)
    rect (200,180,400,25)
    rect(300, 300, 200, 50)

def draw ():                             
                                              
    #Startbutton nach S.Hefti 
    if mouseX >= 300 and mouseX <= 300 + 200 and mouseY >= 300 and mouseY <= 300 + 50 and mousePressed == True:
        drawMenu()
        drawAuswahl() 
        
    #Button Auswahl 50kg
    if mouseX >= 100 and mouseX <= 100 + 25 and mouseY >= 150 and mouseY <= 150 + 25 and mousePressed == True:
            draw50kg() 
    
    #Button Auswahl 70kg 
    if mouseX >= 350 and mouseX <= 350 + 25 and mouseY >= 150 and mouseY <= 150 + 25 and mousePressed == True:
        draw70kg()
        
    #Button Auswahl 90kg 
    if mouseX >= 600 and mouseX <= 600 + 25 and mouseY >= 150 and mouseY <= 150 + 25 and mousePressed == True:
        draw90kg()
        
def drawMenu ():                       #Menü
    
    w = "Weight of the falling person?" #Menütext 
    h = "Height of the fall?" 
    
    background (0,0,0)                   #Fensterfarbe 
    fill (255, 255, 255)                 
    textSize (30) 
    textAlign (CENTER) 
    text (w, 400, 100)  
    text (h, 400, 300)

def drawAuswahl ():                        #Auswahlmöglichkeiten  
    
    textSize (20)
    rect (100,150,25,25)
    text ("50 kg", 200, 175) 
    rect (350,150,25,25)
    text ("70 kg", 450, 175) 
    rect (600,150,25,25)
    text ("90 kg", 700, 175) 
    
    rect (100,350,25,25)
    text ("2 m", 200, 375)
    rect (350,350,25,25)
    text ("4 m", 450, 375)
    rect (600,350,25,25)
    text ("6 m", 700, 375)

def draw50kg (): 
     textSize (20)
     rect (100,150,25,25)
     fill (130) 
     text ("50 kg", 200, 175)

def draw70kg (): 
     textSize (20)
     rect (350,150,25,25)
     fill (130) 
     text ("70 kg", 450, 175)

def draw90kg (): 
     textSize (20)
     rect (600,150,25,25)
     fill (130) 
     text ("90kg", 700, 175)
