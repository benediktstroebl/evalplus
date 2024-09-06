def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    temp = a.replace(" ","")
    temp = temp.replace("","")
    if (a.find(b) != -1 or a.find(b[1:] + b[:1]) != -1 or a.find(b[2:] + b[:2]) != -1 or a.find(b[-1:] + b[:-1]) != -1 or a.find(b[-2:] + b[:-2]) != -1 or a.find(b[-3:] + b[:-3]) != -1 or a.find(b[:-4] + b[-4:]) != -1):
        return True
    else:
        return False