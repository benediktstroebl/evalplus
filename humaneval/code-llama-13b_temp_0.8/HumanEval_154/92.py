
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    try:
        fst = a
        scd = b
        if len(fst) < len(scd):
            return False
        else:
            first_letter_index = fst.find(scd[0])
            if first_letter_index == -1:
                return False
            elif first_letter_index + len(scd) > len(fst):
                return False
            else:
                for i in range(len(scd)):
                    if fst[first_letter_index + i] != scd[i]:
                        return False
                return True
    except:
        return False

