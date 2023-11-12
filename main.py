
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
Colors = {
RED:'\u001b[41m',
BLUE:'\u001b[44m',
WHITE:'\u001b[47m',
END:'\u001b[0m'}#Не знаю, зачем существует этот словарь

#Все функции находятся в самом низу(вариант)



def Task_1():
    class ColorStrip:
        ENDCOLOR = '\u001b[0m'
        WIDTH = 6
        def __init__(self, hight: int , color: str) -> None:
            self.hight = hight
            self.color = color
        def __str__(self) -> str:
            resultstring = ''
            me = self
            for i in range(me.hight):
                resultstring += f'{me.color}{" "*me.WIDTH}{me.ENDCOLOR}\n' 
            
            return resultstring  
    HIGHT  = 1
    #stp = strip
    redstp = ColorStrip(HIGHT, Colors[RED])
    whitestp = ColorStrip(HIGHT, Colors[WHITE])
    bluestp = ColorStrip(HIGHT, Colors[BLUE])
    print(f'{redstp}{whitestp}{bluestp}')
#Задание 2. просто задание 2
def Task_2final():
    countofpatterns = 5#Количество узоров 
    _squresize=squresize=14#размер поля с узорами
    stepper = 0
    for i in range(squresize//2):
        odd= False
        stepper+=1
        resultline=(stepper)*" " +Colors[WHITE]+" "+Colors[END]+''
        _squresize-=1
        approuchstepper = _squresize-stepper
        for b in range(countofpatterns*3):
           resultline+=(approuchstepper)*" " +Colors[WHITE]+" "+Colors[END]+''
           approuchstepper= squresize - approuchstepper-2
        print(resultline)
    _squresize=squresize=14#размер поля с узорами
    stepper = squresize//2+1
    for i in range(squresize//2):
        stepper-=1
        resultline=(stepper)*" " +Colors[WHITE]+" "+Colors[END]+''
        approuchstepper = _squresize-stepper*2
        for b in range(countofpatterns*3):
           resultline+=(approuchstepper)*" " +Colors[WHITE]+" "+Colors[END]+''
           approuchstepper= squresize - approuchstepper-2
        print(resultline)
class Point:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def setColor(self, color):
        self.color = color
    def showColor(self):
        return self.color
    def showPosition(self):
        return (self.x, self.y)
class PointsField:#Поле точек будет квадратным!
    basecolor = Colors[END]
    def __init__(self,sidesize,spacescount=4):
        self.spacescount = spacescount
        massive = []
        self.sidesize = sidesize
        for x in range(sidesize):
            massive.append([])
            for y in range(sidesize):
                massive[x].append(Point(x,y,self.basecolor))
        self.pointsmassive = massive

    def setpointcolor(self,x,y, color):
            self.pointsmassive[round(x)][round(y)].setColor(color)
    def print(self):
        for deltay in range(self.sidesize):
            y = self.sidesize - deltay -1
            l=""+END
            for x in range(self.sidesize):
                l+= str(self.pointsmassive[x][y].showColor()) + " "*self.spacescount+END+""
            print(l)
        print()
    def printwithcoordinate(self):
        for deltay in range(self.sidesize):
           y = self.sidesize - deltay -1
           l=str(y)+END
           for x in range(self.sidesize):
               l+= str(self.pointsmassive[x][y].showColor()) + " "*self.spacescount+END+""
           print(l)
        n= ''
        for b in range(self.sidesize):
            n+= f"  {b%100//10}{b%10}"
        print(n)
    def drowlinebyrule(self, function):
        for x in [i/10 for i in range(1,(self.sidesize-1)*10)]:
            funcres = function(x)
            if (0<= round(funcres)<self.sidesize) and (0<= round(x) <self.sidesize):
                self.setpointcolor(x,funcres , Colors[WHITE])   





 #Задание 2. Если воспользоваться функцией для задания 3(но узор не повторяется)
def Task_2_interestingtest():
    hight = 30
    field = PointsField(hight,1)
    field.drowlinebyrule(lambda x:abs((x-hight//2)))
    field.drowlinebyrule(lambda x:15-abs((x-hight//2)))
    field.print()
#Задание 3
def Task_3():
    hight = 25
    field = PointsField(hight,4)
    field.drowlinebyrule(lambda x:2*x)
    field.printwithcoordinate()
#задание 4
def Task_4():
    evenSum = 0
    unevenSum = 0
    fl = open('sequence.txt')
    text = fl.read().split('\n')
    for linenum in range(len(text)):
        if linenum%2 == 0:
            evenSum+= abs(float(text[linenum]))
        else:
            unevenSum+= abs(float(text[linenum]))
    print(f'сумма чисел на чётных:{evenSum} и нечётных { unevenSum} позициях' ) 
    
    fl.close()
        




#-----Задание 1:-----
#Task_1()
#-----Задание 2. Если воспользоваться функцией для задания 3(но узор не повторяется):-----
#Task_2_interestingtest()

#-----Задание 2. просто задание 2:-----
#Task_2final()

#-----Задание 3:-----
#Task_3()
#задание 4
#Task_4()

    
    
                
                

