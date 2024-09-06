
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if (len(a)<len(b)):
        return False
    elif len(a)==len(b):
        return a==b
    elif len(a)>(len(b)*2):
        return False
    else:
        sublist=a[0:len(b)]
        flag=0
        for i in range(1,len(a)-len(b)+1):
            if (sublist==b):
                flag=1
                break
            sublist=sublist[1:len(b)]+sublist[0]
        if (flag==1):
            return True
        else:
            return False
