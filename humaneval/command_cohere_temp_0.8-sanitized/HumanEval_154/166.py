def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    b = b.strip(".")
    b = b.strip("!")
    b = b.strip("?")
    b = b.strip(",")
    b = b.strip("'")
    return (a.find(b) >= 0) or any(a.find( rotated_b ) >= 0 for rotated_b in rotated_b_generator(b))