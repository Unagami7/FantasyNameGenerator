import random

w=random.randint(1,2)

if w==1:
    
    x = random.randint(1,47)
    # První začáteční
    if x==1:
        #print("a")
        y= "A"
    elif x==2:
        #print("b")
        y= "B"
    elif x==3 or x==35:
        #print("c")
        y= "C"
    elif x==4 or x ==36:
        #print("d")
        y= "D"
    elif x==5:
        #print("e")
        y= "E"
    elif x==6:
        #print("f")
        y= "F"
    elif x==7:
        #print("g")
        y= "G"
    elif x==8:
        #print("h")
        y= "H"
    elif x==9:
        #print("i")
        y= "I"
    elif x==10:
        #print("j")
        y= "J"
    elif x==11 or x==37:
        #print("k")
        y= "K"
    elif x==12:
        #print("l")
        y= "L"
    elif x==13 or x==38:
        #print("m")
        y= "M"
    elif x==14 or x==39:
        #print("n")
        y= "N"
    elif x==15:
        #print("o")
        y= "O"
    elif x==16 or x==40:
        #print("p")
        y= "P"
    elif x==17 or x==41:
        #print("q")
        y= "Q"
    elif x==18 or x==42:
        #print("r")
        y= "R"
    elif x==19:
        #print("s")
        y= "S"
    elif x==20 or x==43:
        #print("t")
        y= "T"
    elif x==21:
        #print("u")
        y= "U"
    elif x==22 or x==44:
        #print("v")
        y= "V"
    elif x==23 or x==45:
        #print("w")
        y= "W"
    elif x==24:
        #print("x")
        y= "X"
    elif x==25:
       #print("y")
       y= "Y"
    elif x==26:
        #print("z")
        y= "Z"
    elif x==27:
        #print("ch")
        y= "Ch"
    elif x==28 or x==46:
        #print("dr")
        y= "Dr"
    elif x==29:
        #print("bh")
        y= "Bh"
    elif x==30:
        #print("ll")
        y= "Ll"
    elif x==31:
        #print("st")
        y= "St"
    elif x==32:
        #print("th")
        y= "Th"
    elif x==33:
        #print("gh")
        y= "Gh"
    elif x==34 or x==47:
        #print("kh")
        y= "Kh"
    else:
        #print("error")
        y= "Error"
    
    e = random.randint(1,24)
    # Druhý samohláskový
    if e==1 or e==19:
        #print("a")
        q="a"
    elif e==2 or e==20:
        #print("e")
        q="e"
    elif e==3:
        #print("i")
        q="i"
    elif e==4 or e==22:
        #print("o")
        q="o"
    elif e==5:
        #print("u")
        q="u"
    elif e==6 or e==21:
        #print("y")
        q="y"
    elif e==7 or e==23:
        #print("ao")
        q="ao"
    elif e==8:
        #print("ea")
        q="ea"
    elif e==9:
        #print("ae")
        q="ae"
    elif e==10:
        #print("aa")
        q="aa"
    elif e==11:
        #print("ii")
        q="ii"
    elif e==12:
        #print("ee")
        q="ee"
    elif e==13:
        #print("oo")
        q="oo"
    elif e==14:
        #print("au")
        q="au"
    elif e==15:
        #print("ye")
        q="ye"
    elif e==16 or e==24:
        #print("ía")
        q="ía"
    elif e==17:
        #print("ue")
        q="ue"
    elif e==18:
        #print("io")
        q="io"
    else:
        #print("-error-")
        q="error"
    
    r=random.randint(1,45)
    # Třetí souhláskový
    if r==1:
        #print("c")
        k = "c"
    elif r==2 or r==36:
        #print("d")
        k = "d"
    elif r==3:
        #print("f")
        k = "f"
    elif r==4 or r==37:
        #print("g")
        k = "g"
    elif r==5:
        #print("h")
        k = "h"
    elif r==6:
        #print("j")
        k = "j"
    elif r==7:
        #print("k")
        k = "k"
    elif r==8:
        #print("l")
        k = "l"
    elif r==9:
        #print("m")
        k = "m"
    elif r==10:
        #print("n")
        k = "n"
    elif r==11:
        #print("p")
        k = "p"
    elif r==12:
        #print("q")
        k = "q"
    elif r==13 or r==38:
        #print("r")
        k = "r"
    elif r==14 or r==39:
        #print("s")
        k = "s"
    elif r==15:
        #print("t")
        k = "t"
    elif r==16:
        #print("v")
        k = "v"
    elif r==17:
        #print("w")
        k = "w"
    elif r==18 or r==40:
        #print("x")
        k = "x"
    elif r==19:
        #print("z")
        k = "z"
    elif r==20 or r==41:
        #print("dd")
        k = "dd"
    elif r==21:
        #print("ss")
        k = "ss"
    elif r==22:
        #print("tt")
        k = "tt"
    elif r==23:
        #print("rr")
        k = "rr"
    elif r==24:
        #print("kk")
        k = "kk"
    elif r==25:
        #print("ll")
        k = "ll"
    elif r==26 or r==42:
        #print("nn")
        k = "nn"
    elif r==27:
        #print("ch")
        k = "ch"
    elif r==28 or r==43:
        #print("dr")
        k = "dr"
    elif r==29 or r==44:
        #print("kh")
        k = "kh"
    elif r==30 or r==45:
        #print("gh")
        k = "gh"
    elif r==31:
        #print("bh")
        k = "bh"
    elif r==32:
        #print("th")
        k = "th"
    elif r==33:
        #print("st")
        k = "st"
    elif r==34:
        #print("rd")
        k = "rd"
    elif r==35:
        #print("lf")
        k = "lf"
    else:
        #print("error")
        k = "-error-"
        
    # Čtvrtý konečný
    s = random.randint(1,24)
    if s==1:
        #print("a")
        a = "a"
    elif s==2:
        #print("e")
        a= "e"
    elif s==3:
        #print("i")
        a= "i"
    elif s==4:
        #print("o")
        a= "o"
    elif s==5:
        #print("u")
        a= "u"
    elif s==6:
        #print("y")
        a= "y"
    elif s==7:
        #print("í")
        a= "í"
    elif s==8:
        #print("umi")
        a= "umi"
    elif s==9 or s==20:
        #print("eus")
        a= "eus"
    elif s==10:
        #print("eton")
        a= "eton"
    elif s==11:
        #print("us")
        a= "us"
    elif s==12:
        #print("imir")
        a= "imir"
    elif s==13 or s==24:
        #print("ahg")
        a= "ahg"
    elif s==14:
        #print("uir")
        a= "uir"
    elif s==15:
        #print("ílt")
        a= "ílt"
    elif s==16 or s==23:
        #print("ionna")
        a= "ionna"
    elif s==17 or s==22:
        #print("itia")
        a= "itia"
    elif s==18:
        #print("icia")
        a= "icia"
    elif s==19 or s==21:
        #print("ia")
        a= "ia"
    else:
        #print("error")
        a="-error"
    print(y+q+k+a)
elif w==2:
    
    x = random.randint(1,47)
    # První začáteční
    if x==1:
        #print("a")
        y= "A"
    elif x==2:
        #print("b")
        y= "B"
    elif x==3 or x==35:
        #print("c")
        y= "C"
    elif x==4 or x ==36:
        #print("d")
        y= "D"
    elif x==5:
        #print("e")
        y= "E"
    elif x==6:
        #print("f")
        y= "F"
    elif x==7:
        #print("g")
        y= "G"
    elif x==8:
        #print("h")
        y= "H"
    elif x==9:
        #print("i")
        y= "I"
    elif x==10:
        #print("j")
        y= "J"
    elif x==11 or x==37:
        #print("k")
        y= "K"
    elif x==12:
        #print("l")
        y= "L"
    elif x==13 or x==38:
        #print("m")
        y= "M"
    elif x==14 or x==39:
        #print("n")
        y= "N"
    elif x==15:
        #print("o")
        y= "O"
    elif x==16 or x==40:
        #print("p")
        y= "P"
    elif x==17 or x==41:
        #print("q")
        y= "Q"
    elif x==18 or x==42:
        #print("r")
        y= "R"
    elif x==19:
        #print("s")
        y= "S"
    elif x==20 or x==43:
        #print("t")
        y= "T"
    elif x==21:
        #print("u")
        y= "U"
    elif x==22 or x==44:
        #print("v")
        y= "V"
    elif x==23 or x==45:
        #print("w")
        y= "W"
    elif x==24:
        #print("x")
        y= "X"
    elif x==25:
       #print("y")
       y= "Y"
    elif x==26:
       # print("z")
        y= "Z"
    elif x==27:
       # print("ch")
        y= "Ch"
    elif x==28 or x==46:
        #print("dr")
        y= "Dr"
    elif x==29:
       # print("bh")
        y= "Bh"
    elif x==30:
       # print("ll")
        y= "Ll"
    elif x==31:
      #  print("st")
        y= "St"
    elif x==32:
       # print("th")
        y= "Th"
    elif x==33:
      #  print("gh")
        y= "Gh"
    elif x==34 or x==47:
      #  print("kh")
        y= "Kh"
    else:
      #  print("error")
        y= "Error"
    
    e = random.randint(1,24)
    # Druhý samohláskový
    if e==1 or e==19:
      #  print("a")
        q="a"
    elif e==2 or e==20:
      #  print("e")
        q="e"
    elif e==3:
      #  print("i")
        q="i"
    elif e==4 or e==22:
       # print("o")
        q="o"
    elif e==5:
   #     print("u")
        q="u"
    elif e==6 or e==21:
     #   print("y")
        q="y"
    elif e==7 or e==23:
     #   print("ao")
        q="ao"
    elif e==8:
     #   print("ea")
        q="ea"
    elif e==9:
    #    print("ae")
        q="ae"
    elif e==10:
     #   print("aa")
        q="aa"
    elif e==11:
     #   print("ii")
        q="ii"
    elif e==12:
     #   print("ee")
        q="ee"
    elif e==13:
      #  print("oo")
        q="oo"
    elif e==14:
      #  print("au")
        q="au"
    elif e==15:
      #  print("ye")
        q="ye"
    elif e==16 or e==24:
    #    print("ía")
        q="ía"
    elif e==17:
     #   print("ue")
        q="ue"
    elif e==18:
      #  print("io")
        q="io"
    else:
      #  print("-error-")
        q=""
    
    r=random.randint(1,45)
    # Třetí souhláskový
    if r==1:
       # print("c")
        k = "c"
    elif r==2 or r==36:
       # print("d")
        k = "d"
    elif r==3:
       # print("f")
        k = "f"
    elif r==4 or r==37:
      #  print("g")
        k = "g"
    elif r==5:
      #  print("h")
        k = "h"
    elif r==6:
      #  print("j")
        k = "j"
    elif r==7:
     #   print("k")
        k = "k"
    elif r==8:
       # print("l")
        k = "l"
    elif r==9:
      #  print("m")
        k = "m"
    elif r==10:
     #   print("n")
        k = "n"
    elif r==11:
     #   print("p")
        k = "p"
    elif r==12:
     #   print("q")
        k = "q"
    elif r==13 or r==38:
      #  print("r")
        k = "r"
    elif r==14 or r==39:
     #   print("s")
        k = "s"
    elif r==15:
    #    print("t")
        k = "t"
    elif r==16:
     #   print("v")
        k = "v"
    elif r==17:
     #   print("w")
        k = "w"
    elif r==18 or r==40:
    #    print("x")
        k = "x"
    elif r==19:
     #   print("z")
        k = "z"
    elif r==20 or r==41:
     #   print("dd")
        k = "dd"
    elif r==21:
       # print("ss")
        k = "ss"
    elif r==22:
       # print("tt")
        k = "tt"
    elif r==23:
     #   print("rr")
        k = "rr"
    elif r==24:
     #   print("kk")
        k = "kk"
    elif r==25:
    #    print("ll")
        k = "ll"
    elif r==26 or r==42:
     #   print("nn")
        k = "nn"
    elif r==27:
     #   print("ch")
        k = "ch"
    elif r==28 or r==43:
     #   print("dr")
        k = "dr"
    elif r==29 or r==44:
     #   print("kh")
        k = "kh"
    elif r==30 or r==45:
     #   print("gh")
        k = "gh"
    elif r==31:
     #   print("bh")
        k = "bh"
    elif r==32:
      #  print("th")
        k = "th"
    elif r==33:
      #  print("st")
        k = "st"
    elif r==34:
       # print("rd")
        k = "rd"
    elif r==35:
    #    print("lf")
        k = "lf"
    else:
     #   print("error")
        k = "-error-"
    print(y+q+k)
else:
    print("ElBigoError")
