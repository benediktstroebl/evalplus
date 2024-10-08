def reverse_delete(s, c):
    # Filter and delete characters in s that are in c
    s = ''.join([x for x in s if x not in c])
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])