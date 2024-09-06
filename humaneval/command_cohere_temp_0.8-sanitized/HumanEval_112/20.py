def reverse_delete(s, c):
    # Calculate the delete operation on s with respect to c
    s = s.replace(c, '')

    # Check if the resulting string is a palindrome
    return s, s == s[::-1]