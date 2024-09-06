
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
    if a_len != b_len:
        return False

    b_list = []
    b_list.append(b)
    for i in range(0, b_len):
        b_list.append(b[i:] + b[:i])

    if b_len == 1:
        return True
    if b_len == 2:
        return False

    for b_item in b_list:
        b_rotation_count = 2
        b_rotation_list = []
        b_rotation_list.append(b_item)
        while b_rotation_count <= a_len:
            b_rotation_list.append(b_item[b_rotation_count:] + b_item[:b_rotation_count])
            b_rotation_count += 1
        for b_rotation in b_rotation_list:
            if b_rotation in a:
                return True

    return False
