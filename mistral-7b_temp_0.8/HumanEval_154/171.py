
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #this is the first part where we check if the words are the same
    if a == b:
        return False
    #this is the second part where we use the recursive function to check if the word is a substring of the second word
    if len(b) <= len(a):
        return a.find(b) != -1

    #this is the third part where we check if the first word is a substring of the second word
    for i in range(len(b)):
        if b.find(a) != -1:
            return True
        b = b[1:] + b[0]
    #this is the fourth part where we check if the words are the same but in reverse order
    if a == b[::-1]:
        return True
    #if all the parts failed then we return false
    return False
