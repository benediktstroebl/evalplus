
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False

    if len(b) == 0:
        return True

    a_freq_char = {}
    b_freq_char = {}

    for letter in a:
        a_freq_char[letter] = a_freq_char.get(letter, 0) + 1

    for letter in b:
        b_freq_char[letter] = b_freq_char.get(letter, 0) + 1

    # print(a_freq_char, b_freq_char)

    for letter in a_freq_char:
        if letter not in b_freq_char or a_freq_char[letter] != b_freq_char[letter]:
            return False

    return True

