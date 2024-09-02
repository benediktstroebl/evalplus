
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    ################ Beginning of Your Code -----------------------------------
    #Your code must be in this function exactly as written
    if len(a) > len(b):
        big = a
        small = b
    else:
        big = b
        small = a
    counter = 0
    for i in range(len(small)):
        if small[i] in big:
            index = big.find(small[i])
            if small[i:] == big[index:index + len(small)]:
                return True
    return False
        
        
    
    
    ################### End of Your Code  -----------------------------------

