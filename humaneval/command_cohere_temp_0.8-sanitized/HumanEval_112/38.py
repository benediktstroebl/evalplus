def reverse_delete(s, c):
    # Filter and delete characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the remaining string is a palindrome
    return s, s == s[::-1]