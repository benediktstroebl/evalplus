def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    temp = set(b)
    for char in a:
        if char not in temp and temp != set():
            return False
        temp.remove(char)

    return not temp