
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(b) == len(a):
        return a == b
    if len(b) > len(a):
        return False
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in range(len(b)):
        templen=len(b)-i
        if templen > len(a):
            return False
        templist=list(b)
        for i in range(templen):
            templist.append(templist.pop(0))
        tempstr=''.join(templist)
        tempres={}
        for i in tempstr:
            if i not in tempres:
                tempres[i]=1
            else:
                tempres[i]+=1
        tempres2={}
        for i in tempres:
            if tempres[i]>1:
                tempres2[i]=tempres[i]
        if tempres2==d:
            return True
    return False

