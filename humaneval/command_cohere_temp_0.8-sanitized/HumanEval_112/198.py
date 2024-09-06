def reverse_delete(s, c):
    """
    Deletes characters in 's' that are also in 'c', and checks if the remainder is a palindrome.
    """
    s = [x for x in s if x not in c]
    return s, s == s[::-1]