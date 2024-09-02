
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #calculate the length of the string a
    la=len(a)
    #calculate the length of the string b
    lb=len(b)
    #if a and b have the same length then the condition is false
    if la==lb:
        return False
    #create a list called b_list
    b_list=[]
    #for b_rotation in range from 0 to len(b)
    for b_rotation in range(lb):
        #append the list b_list with b[b_rotation:] + b[0:b_rotation]
        b_list.append(b[b_rotation:] + b[0:b_rotation])
    #for i in range from 0 to len(a)
    for i in range(la):
        #if a[i:] + a[0:i] is in b_list then return True
        if a[i:] + a[0:i] in b_list:
            return True
    #else return False
    return False
