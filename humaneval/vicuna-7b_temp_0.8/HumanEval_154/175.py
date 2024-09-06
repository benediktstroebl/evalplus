
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    first_word, second_word = a, b
    first_word_len = len(first_word)
    second_word = second_word.lower()
    second_word_len = len(second_word)

    for i in range(second_word_len):
        temp_str = second_word[:i] + second_word[i+1:]
        temp_str = temp_str.lower()
        if any(c in first_word for c in temp_str):
            return True
    return False
