def is_happy(s):
    """
    Check if a string is happy or not. A happy string has at least 3 distinct characters and length
    :param s: string
    :return: boolean
    """
    if len(s) < 3:
        return False
    c1, c2, c3 = s, s[1], s[2]
    for _ in range(3, len(s)):
        if c1 == c2 and c2 == c3:
            return False
        c1, c2, c3 = c2, c3, c1
    return True