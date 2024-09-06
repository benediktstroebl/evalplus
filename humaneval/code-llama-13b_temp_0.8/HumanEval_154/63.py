
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    l1 = len(a)
    l2 = len(b)
    temp = a
    temp2 = b
    count = 0
    for i in range(l1):
        if(l1>l2 and l1>count+l2):
            sub_string = temp[i:i+l2]
            if(sub_string == temp2):
                return True
            else:
                count = count + 1
    return False
