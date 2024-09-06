
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #Your code goes here
    pattern=b
    pattern_l=[]
    pattern_l.append(pattern)
    if len(pattern)<len(a):
        for i in range(1,len(pattern)):
            pattern_l.append(pattern[i:]+pattern[:i])
        for i in pattern_l:
            if i in a:
                return True
    return False
