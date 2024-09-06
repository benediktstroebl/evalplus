def reverse_delete(s, c):
    # Replace characters in s that are in c with None
    s = [x if x not in c else None for x in s]
    # Filter out None characters from s
    s = ''.join(x for x in s if x is not None)
    # Check if s is a palindrome
    return s, s == s[::-1]