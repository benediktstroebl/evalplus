
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    
    if a[0] == a[-1]: #checking if the first and last character are same
        return False

    #for i in range(0,len(a)):
    for j in range(1,len(a)):
        if a[0:j] in b or a[j:] in b:
            return True #if any substring in the array of a is in array b,then return true
        
    return False
