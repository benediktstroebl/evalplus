
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Your code goes here
    pattern = a
    s = b
    pattern_len = len(pattern)
    if pattern_len > len(s):
        return False
    flag = False
    for i in range(len(s)):
        if pattern[0:pattern_len] == s[i:i+pattern_len]:
            flag = True
            break
    return flag

