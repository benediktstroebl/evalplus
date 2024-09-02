
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    dp=set()
    for i in range(len(a)):
        if b[i] in dp:
            return False
        else:
            for i in range(len(b)):
                if b[i] == b[i+1] ^ b[i+2] ^ b[i+3] ^ b[i+4] ^ b[i+5]:
                    dp.add(b[i])
        for i in range(len(b)):
            if not b[i] in dp:
                return False
    return True