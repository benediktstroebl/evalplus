def reverse_delete(s, c):
    # Remove characters in 's' that are present in 'c'
    s = [x for x in s if x not in c]
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])