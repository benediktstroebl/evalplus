
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a)!= len(b):
        return False

    if not b:
        return True

    for i in range(len(a)):
        if a[i] == b[-1]:
            return cycpattern_check(a[i+1:], b[:-1])
        else:
            if a.startswith(b[:-1]):
                return True
            else:
                return False
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
