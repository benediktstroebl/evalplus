
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Step 1:
    # Cyclical pattern
    # Cycle through the string to be checked,
    # i.e. the second string,
    #  checking if it's a substring of the first string,
    # if not, cycle again, and so on.
    # If the string is found to be a substring of the first string,
    #  return True.
    # If after checking all possible cycles,
    #  the result is still False,
    # return False.
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False
