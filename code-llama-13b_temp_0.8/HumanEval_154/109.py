
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # returns a list of substring of word
    def get_substrings(word):
        return [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)]

    # check if substring is cyclically the same with the first word
    def is_cyclic_substring(word, sub):
        return sub == word[len(word) - len(sub):] + word[:len(word) - len(sub)]

    # Check if any of the rotations of the second word is a substring of the first word
    # return True if any of the rotations of the second word is a substring of the first word
    for sub in get_substrings(b):
        if is_cyclic_substring(a, sub):
            return True
    return False
