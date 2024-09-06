
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    def get_rotation(str):
        rotation = []
        for i in range(0,len(str)):
            rotation.append(str[i:] + str[:i])
        return rotation

    if len(a) < len(b):
        return False

    a_split = get_rotation(a)
    if b in a_split:
        return True
    else:
        return False
