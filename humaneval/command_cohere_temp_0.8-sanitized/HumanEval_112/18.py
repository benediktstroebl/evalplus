def reverse_delete(s, c):
    """
    Removes characters from s that are present in c, then checks if the resulting string is a palindrome.
    """
    s = [x for x in s if x not in c]
    return s, s == s[::-1]