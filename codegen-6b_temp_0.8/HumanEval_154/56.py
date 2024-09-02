
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if(len(b)>len(a)):
        return False
    first = a[:len(b)]
    find_word = False
    for i in range(len(a)-len(b)+1):
        if(first==b or first==b[::-1]):
            find_word = True
            break
        first = first[1:] + first[0]
    return find_word

