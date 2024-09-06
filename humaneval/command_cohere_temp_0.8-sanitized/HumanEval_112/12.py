def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = [c for c in s if c not in c]
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])