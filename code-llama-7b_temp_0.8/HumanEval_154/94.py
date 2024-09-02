
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    #
    if a.find(b) >= 0:
        return True
    else:
        # Remove all occurences of the alphabet a and then remove all occurences of the alphabet b and compare
        # Then, remove all occurences of the alphabet b and then remove all occurences of the alphabet a and compare
        # Then, remove all occurences of the alphabet b and then remove all occurences of the alphabet a and reverse the string
        # Then, remove all occurences of the alphabet a and then remove all occurences of the alphabet b and reverse the string
        # Then, remove all occurences of the alphabet a and then remove all occurences of the alphabet b and reverse the string
        # Then, remove all occurences of the alphabet a and then remove all occurences of the alphabet b and reverse the string

        return (a.replace(a, "") == b.replace(b, "") or a.replace(b, "") == b.replace(a, "") or a.replace(b, "")[::-1] == b.replace(a, "")[::-1] or a.replace(a, "")[::-1] == b.replace(b, "")[::-1] or a.replace(b, "")[::-1] == b.replace(a, "")[::-1] or a.replace(a, "")[::-1] == b.replace(b, "")[::-1])


