def reverse_delete(s, c):
    # Delete characters in s that are in c
    s = ''.join([x for x in s if x not in c])
    
    # Check if the result string is a palindrome
    is_palindrome = s == s[::-1]
    
    return s, is_palindrome