
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #The idea here is to build a string with all the rotations of the string and then check if the string is a substring of the other string

    # Get rotations of the string b
    rotation=[]
    for i in range(len(b)):
        rotation.append(b[i:]+b[:i])
    rotation_str=''.join(rotation)

    #If string b is a substring of string a
    if b in a:
        return True

    #if one of the rotations of b is a substring of string a
    elif rotation_str in a:
        return True

    else:
        return False
    
