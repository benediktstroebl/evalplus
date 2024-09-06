def cycpattern_check(a, b):
    str1 = a
    str2 = b
    if len(str2) > len(str1):
        return False
    str2 = str2 + str2
    return any(str2.startswith(x) for x in str1)