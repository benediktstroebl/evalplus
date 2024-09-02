
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    s1 = a
    s2 = b
    if len(s1) == len(s2):
        #print "1st is equal to 2nd"
        for i in range(len(s1)):
            #print "s1 is ",s1, "s2 is ", s2
            if s1[i] == s2[0]:
                match = True
            else:
                match = False
            s2 = s2[1:]
            s2 += s1[0]
            #print "new s2 is ", s2, "match is ", match
            if match == True:
                break
    else:
        #print "1st is not equal to 2nd"
        pass
    return match
