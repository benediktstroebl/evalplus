
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Cycle through the characters of the first word
    for i in range(len(a)):
        # Check if the current character and the next character are the same
        if a[i] == a[i + 1]:
            # If they are, check if the current character and the second last character are the same
            if a[i] == a[len(a) - 1]:
                # If they are, return True
                return True

    # If the above loop doesn't return True, cycle through the characters of the second word
    for i in range(len(b)):
        # Check if the current character and the next character are the same
        if b[i] == b[i + 1]:
            # If they are, check if the current character and the second last character are the same
            if b[i] == b[len(b) - 1]:
                # If they are, return True
                return True

    # If none of the above loops return True, return False
    return False
