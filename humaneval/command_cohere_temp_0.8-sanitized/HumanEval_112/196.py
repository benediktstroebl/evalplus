def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same value as s (initialise with empty string)
    
    for i, char in enumerate(s):
        if char not in delete:
            palindrome += char
    
    return palindrome, palindrome == palindrome[::-1]