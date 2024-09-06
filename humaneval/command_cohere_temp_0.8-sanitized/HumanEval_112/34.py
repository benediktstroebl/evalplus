def reverse_delete(s, c):
    """
    Removes characters from s that are in c, then checks if the result is a palindrome.
    """
    s = [char for char in s if char not in c]
    return s, s == s[::-1]