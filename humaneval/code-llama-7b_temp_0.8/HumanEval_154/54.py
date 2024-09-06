
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # base cases
    if len(a) == 0 or len(b) == 0:
        return False
    if len(b) > len(a):
        return False

    # for each char in the first string
    # take that char and each rotation of that char
    # check if any of them are in the second string
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j%len(a)] == b[0]:
                # find first index where the first char in b is found
                b_first_index = a.find(b[0])
                if b[0:i] == a[b_first_index:b_first_index + i]:
                    # check if the rotation of the second string is in the first string
                    # check first char in b
                    if b[0:i] in a:
                        return True
    return False
