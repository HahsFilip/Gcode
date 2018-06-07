file = open("1002.ngc", "a+")
def makeFile(path):
    code = []
    n = 50
    for line in xyz:
        print(line)
        code.append("N" + str(n) + " G1 X" + str(line[0]) + " Y" + str(line[1]))
        n += 1
    print(code)


def cutTriangle(x1,y1,x2,y2,i):
    path = []
    slope = round(abs((x2-x1)/(y2-y1)),4)
    h = 0
    step = round((x2-x1)/i, 4)
    j = x1
    path.append([x1,y1])
    dH = round(slope*step,4)
    while j <= x2:
        h += dH
        path.append([j, y1])
        path.append([j, y1 + h])
        j += step
        path.append([j, y1 + h])
        path.append([j, y1])
        j += step


    return path

xyz = cutTriangle(-5,-2,-1,3,100)
code = []
n = 50
for line in xyz:
    print(line)
    code.append("N" + str(n) + " G1 X" +   str(line[0]) + " Y" + str(line[1]))
    n +=1
print(code)


for ln in code:
    file.write(ln + "\r\n" )
