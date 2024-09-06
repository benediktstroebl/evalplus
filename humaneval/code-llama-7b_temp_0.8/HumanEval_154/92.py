
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #here we define the function to calculate the number of times the string has to be rotated
    def rotate(a):
        if len(a) % 2 == 0:
            return len(a) / 2
        else:
            return (len(a) + 1) / 2

    # the function to check if the second string is a substring in the first string
    def substring(a , b):
        if a in b:
            return True
        else:
            return False

    # the function to check if all the rotation of the second string are substring in the first string
    def check(a,b):
        for i in range(0 , rotate(b)):
            if substring(b[i:],a):
                continue
            else:
                return False
        return True

    return check(a,b)
