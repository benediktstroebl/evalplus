def reverse_delete(s, c):
    """
    Removes characters from s that are in c, and checks if the resulting string is a palindrome.
    """
    s = [char for char in s if char not in c]
    reversed = s[::-1]
    equal = all(x == y for x, y in zip(s, reversed))
    return (''.join(s), equal)