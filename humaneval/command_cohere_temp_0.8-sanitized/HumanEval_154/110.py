def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    b = b.strip(".")
    b = b.strip("?)")
    b = b.strip("..")
    ans = False
    if len(a) < len(b):
        return ans
    for i in range(len(b)):
        temp = b[0:] + b[1:i+1] + b[i+1:]
        if a.find(temp) != -1:
            ans = True
            break
    return ans