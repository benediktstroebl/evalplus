def reverse_delete(s, c):
    """
    Deletes characters in 's' that are also in 'c', and checks if the resulting string is a palindrome.
    """
    s = set(s) - set(c)
    return s, s == s[::-1]