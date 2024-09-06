def cycpattern_check(a, b):
    str1 = a
    str2 = b
    if len(str2) > len(str1):
        return False
    temp = str2 + str2
    return temp in str1