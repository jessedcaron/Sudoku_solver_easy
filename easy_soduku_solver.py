#puzzle 1
grid = {            #sample data(left to right, up to down. 0=blank)
    "box11" : 6,    #box1
    "box12" : 0,
    "box13" : 5,
    "box21" : 4,
    "box22" : 0,
    "box23" : 1,
    "box31" : 2,
    "box32" : 0,
    "box33" : 7,

    "box14" : 8,    #box2
    "box15" : 0,
    "box16" : 0,
    "box24" : 0,
    "box25" : 2,
    "box26" : 3,
    "box34" : 0,
    "box35" : 1,
    "box36" : 0,

    "box17" : 0,    #box3
    "box18" : 4,
    "box19" : 2,
    "box27" : 0,
    "box28" : 8,
    "box29" : 0,
    "box37" : 0,
    "box38" : 0,
    "box39" : 6,

    "box41" : 5,    #box4
    "box42" : 4,
    "box43" : 0,
    "box51" : 0,
    "box52" : 0,
    "box53" : 2,
    "box61" : 0,
    "box62" : 0,
    "box63" : 0,

    "box44" : 0,   #box5 
    "box45" : 0,
    "box46" : 2,
    "box54" : 1,
    "box55" : 0,
    "box56" : 4,
    "box64" : 9,
    "box65" : 0,
    "box66" : 0,

    "box47" : 0,    #box6
    "box48" : 0,
    "box49" : 0,
    "box57" : 3,
    "box58" : 0,
    "box59" : 0,
    "box67" : 0,
    "box68" : 6,
    "box69" : 4,

    "box71" : 1,    #box7
    "box72" : 0,
    "box73" : 0,
    "box81" : 0,
    "box82" : 2,
    "box83" : 0,
    "box91" : 8,
    "box92" : 7,
    "box93" : 0,

    "box74" : 0,    #box8
    "box75" : 4,
    "box76" : 0,
    "box84" : 5,
    "box85" : 8,    
    "box86" : 0,     
    "box94" : 0,
    "box95" : 0,
    "box96" : 6,

    "box77" : 8,    #box9
    "box78" : 0,
    "box79" : 3,
    "box87" : 6,
    "box88" : 0,
    "box89" : 9,
    "box97" : 4,
    "box98" : 0,
    "box99" : 5
	}


checkv=1
chechh=1
success=0
fail=-1
timesthrough=0
tempbox=""

def secondlevel_search(solved):   
    starth=1
    startv=1
    search=[1,2,3,4,5,6,7,8,9]
    moveh=0
    movev=0
    counterbox=1
    counter=1
    flag=0
    
    while counter<10: # ADVANCE  THROUGH EACH 3x3 box
        search=[1,2,3,4,5,6,7,8,9]
        for target in search:       #pulls each to # search in 3x3 box. 
            movev=startv
            moveh=starth
            counterbox=1
            flag=0
            while(counterbox<=9):           #searches each 3x3 box
                tempbox="box"+str(movev)+str(moveh)
                if grid[tempbox]==target:
                    flag=1                  #if found mark flag
                moveh+=1
                if moveh>(starth+2):        #when reaches border 3x3 box. Reset to next line
                    moveh=starth
                    movev+=1
                counterbox+=1
            if flag==0:                 #if not found then _solve that digit in box
                solved=secondlevel_solve(startv,starth,target,solved)  
        counter+=1
        starth+=3
        if starth>8:
            starth=1
            startv+=3
    return solved

def secondlevel_solve(startv,starth,target,solved): 
    x=1
    vert=startv             #stores the starting place of the search (vert)
    hor=starth               #stores the starting place of the search (hor)
    listofblanks=[]
    possiblesolutions=1
    item=""
    while x<10:
        tempbox="box"+str(vert)+str(hor)   #searches the 3x3 box for blank boxes
        if grid[tempbox]==0:
            listofblanks.append(str(tempbox))   #stores blank boxes into a list
        x+=1
        hor+=1
        if hor>(starth+2):             #when reaches border 3x3 box. Reset to next line
            hor=starth
            vert+=1
    possiblesolution=0
    for item in listofblanks:      #load each blank
        grid[item]=target           #loads # to solve inbox each blank spot
        hori=item[4:5]              #get the cordinate [hor]
        verti=item[3:4]         #get the cordinate [vert]
        findduplicates=0
        checkh=1
        while checkh<=9:
            tempbox="box"+str(verti)+str(checkh)   #looks for duplicates in each colum
            if grid[tempbox]==target:
                findduplicates+=1 
            checkh+=1
        checkv=1
        while checkv<=9:
            tempbox="box"+str(checkv)+str(hori)  #looks for duplicates in each row
            if grid[tempbox]==target:
                findduplicates+=1 
            checkv+=1
        if findduplicates!=2:        #if duplicates reset box to 0(blank)
            grid[item]=0
        if findduplicates==2:       #if no duplicates then it's a potental answer
            possiblesolution+=1      #stores the potential answer for later
            solutionsave=item
        grid[item]=0
    if possiblesolution==1:         #if there is only one poss solution then it sets the box
        grid[solutionsave]=target
        #print(grid[item])   #this prints the solved box  
        solved+=1                  #increments solved 1
    if possiblesolution!=1:     #if there is not one poss solution then reset the box to blank
        grid[item]=0
    return solved

#Execute starts
while fail<=success:     #script will run until it's isn't solving any longer
    fail+=1
    success=secondlevel_search(success)
    timesthrough+=1

    
print("Solved: "+success)    
#print("Times Through:")  #optionally prints the numbers of times the loop was run
#print(timesthrough)
print(grid)


        



    
