
#My variant is 3
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
Colors = {
RED:'\u001b[41m',
BLUE:'\u001b[44m',
WHITE:'\u001b[47m',
END:'\u001b[0m'}#Не знаю, зачем существует этот словарь

#-----Задание 1:-----
DrowFlag()
#-----Задание 2. Если воспользоваться функцией для задания 3(но узор не повторяется):-----
#drowPattern_ByFunction()

#-----Задание 2. просто задание 2:-----
#drowPattern_Repiteldy()

#-----Задание 3:-----
#drowFunction()
def DrowFlag():
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
def drowPattern_ByFunction():
    hight = 30
    field = PointsField(hight,1)
    field.drowlinebyrule(lambda x:6+abs((x-hight)//2))
    field.drowlinebyrule(lambda x:20-abs((x-hight)//2))
    field.print()
#Задание 2. просто задание 2
def drowPattern_Repiteldy():
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
#Задание 3
def drowFunction():
    hight = 30
    field = PointsField(hight,1)
    field.printwithcoordinate(lambda x:2*x)
    field.print()





    
    
                
                


        









'''for i in range(6):
    if i < 3:
        print(f'{BLUE}{"  " * (2 * i + 2)}{WHITE}{"  " * (14 - 2 * i)}{END}')
    else:
        print(f'{BLUE}{"  " * (12 - 2 * i)}{RED}{"  " * (4 + 2 * i)}{END}')'''


# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = i ** 3

# step = round(abs(result[0] - result[9]) / 9, 2)
# print(step)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8-i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(int(plot_list[i][j])) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '!!'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')

# for i in range(10):
#     #print(plot_list[i])
#     pass

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# print(list)