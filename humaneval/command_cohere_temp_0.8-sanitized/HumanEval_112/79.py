def reverse_delete(s, c):
    # Filter s to remove characters in c
    s = ''.join(x for x in s if x not in c)
    
    # Check if the resulting string is a palindrome
    return s, s == s[::-1]