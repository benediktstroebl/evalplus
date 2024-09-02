
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    
    def is_substr(a, b):
        ''''Checks whether b is a substring of a or not.'''
        i = 0
        while i < len(a):
            if a[i:i+len(b)] == b:
                return True
            i += 1        
        return False
    
    def is_rotate(a, b):
        ''''Checks whether b is a rotation of a or not'''
        return is_substr(a, b) and is_substr(b, a)
    
    if is_substr(a, b) or is_rotate(a, b):
        return True
    else:
        return False
    