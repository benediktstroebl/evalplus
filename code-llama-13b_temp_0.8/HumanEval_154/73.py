
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # return True or False
    if len(a)<=len(b):
        return False
    blist=list(b)
    i=0
    while len(blist)>i:
        a=a+a[0]
        b=b+b[0]
        i+=1
    if b in a:
        return True
    return False

    #loop1=len(a)
    #loop2=len(b)
    #temp=0
    #if loop1<loop2:
    #   return False
    #while loop1>0:
    #   loop1-=1
    #   if b in a:
    #       return True
    #   a=a+a[0]
    #   b=b+b[0]
    #   temp+=1
    #   if temp==loop2:
    #       return False
