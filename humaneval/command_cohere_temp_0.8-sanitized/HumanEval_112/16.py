def reverse_delete(s, c):
    """
    Deletes characters in 's' that are present in 'c', and checks if the resulting string is a palindrome.
    """
    s = [char for char in s if char not in c]
    return s, s == s[::-1]