def reverse_delete(s, c):
    """
    Deletes characters in s that are present in c, then checks if the result is a palindrome.
    """
    s = [x for x in s if x not in c]
    palindrome = s == s[::-1]
    return ("".join(s), palindrome)