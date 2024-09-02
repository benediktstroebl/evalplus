
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # TODO - Add Docstring
    # TODO - Add More Cases
    def cycpattern_check_helper(first_string, second_string):
        second_string_len = len(second_string)
        for i in range(len(first_string)):
            if first_string[i:i+second_string_len] == second_string:
                return True
            if first_string[i:i+second_string_len] == reverse_string(second_string):
                return True
        return False

    def reverse_string(string):
        return string[::-1]

    return cycpattern_check_helper(a,b)
