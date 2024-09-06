
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    #Dict with number of times an alphabet is seen in b
    seen_b = {i : 0 for i in set(b)}

    for char in b:
        seen_b[char] += 1

    #Dict with number of times an alphabet is seen in a
    seen_a = {i : 0 for i in set(a)}

    for char in a:
        seen_a[char] += 1

    if seen_b == seen_a:
        return True

    for i in range(len(a)):
        if a[i] in b:
            for j in range(len(b)):
                if i + j < len(a) and a[i + j] == b[j]:
                    pass
                else:
                    break
            else:
                return True

    return False

