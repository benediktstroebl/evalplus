def reverse_delete(s, c):
    # Remove all characters in s that match c
    result = ''.join(c if char != c else char for char in s)
    
    # Check if the reversed string matches s
    return (result, result == s[::-1])
char = "a"