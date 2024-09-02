
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # pylint: disable=R0912,R1705
    def check_substr(s, substr):
        """
        :type s: str
        :type substr: str
        :rtype: bool
        """
        if len(s) < len(substr):
            return False
        if len(s) == len(substr):
            return s == substr
        return s.find(substr) != -1
    def check_rotation(s, substr):
        """
        :type s: str
        :type substr: str
        :rtype: bool
        """
        if len(s) < len(substr):
            return False
        if len(s) == len(substr):
            return s == substr
        return check_substr(s+s, substr)
    return check_substr(a, b) or check_rotation(a, b)
