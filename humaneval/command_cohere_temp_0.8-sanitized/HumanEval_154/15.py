def cycpattern_check(a, b):
    str1 = a
    str2 = b
    if len(str2) >= len(str1):
        return False
    temp = str1[:len(str2)]
    temp = temp.upper()
    if str2 in temp or str2.upper() in temp:
        return True
    return any(x == str2 or x.upper() == str2.upper() for x in str1.split(str2))