import re 

def remove(list): 
    pattern = '[^A-Z]'
    #pattern = '[1-9]'
    #a= re.sub('[^a-zA-Z0-9.?]',' ',a)
    list = [re.sub(pattern, '', i) for i in list] 
    return list

def strToGrid(str, k): 
    temp = ""
    for i in range(len(str)): 
        if i %k == 0: 
            sub = str[i:i+k] 
            lst = [] 
            for j in sub: 
                if (j != ""):lst.append(j) 
            temp += ''.join(lst)
            temp.strip("")
            temp += "\n"
    return temp.strip()
  
def solve(a):
    size = 10
    a = a.replace("0","O")
    a = a.replace("11","U")
    a = a.replace("7","Z")
    a = a.replace("Y.","")
    a = a.replace("-","")
    a = a.replace("!","I")
    a = a.replace("l","I")
    #c = a.strip("").split("\n")
    d = a.splitlines()
    while("" in d) : 
        d.remove("") 
    if(len(d[0]) < 25):
        d.pop(0)
    c = []
    for items in d:
        item = items.strip("").split(" ")
        for x in item:
            if(len(x) > 0):
                c.append(x)
    c = remove(c)
    c = list(filter(None, c))
    
    n = len(c)
    totalStr = ""

    for i in range(0,n-1):
        if(len(totalStr) >= 100):
            break;
        else:
            totalStr += c[i]

    temp = c[i:]
    m = strToGrid(totalStr, size) 
    w = ""
    count = 0

    for i in temp:
        if(len(i)>1 and count < 12):
            w += i + "\n"
            count += 1
    return m,w

if __name__=='__main__':
    input = ""
    matrix,words=solve(input)