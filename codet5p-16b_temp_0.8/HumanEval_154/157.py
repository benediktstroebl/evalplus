
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    a_len = len(a)
    b_len = len(b)

    if b_len == 1:
        return True
    else:
        for i in range(0,a_len):
            j = i
            k = j
            count = 0
            while j < a_len:
                if a[j] == b[k]:
                    count += 1
                    j += 1
                    k += 1
                else:
                    k += 1
                    break
            if count == b_len:
                return True
        return False
        













