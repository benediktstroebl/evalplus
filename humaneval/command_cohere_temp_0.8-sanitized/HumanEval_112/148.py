def reverse_delete(s, c):
    # Calculate the delete operation on s with c
    s = [x for x in s if x not in c]
    
    # Check if the resulting string is a palindrome
    return (s, s == s[::-1])