def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same prefix as s (sliced with :0)
    
    for char in s:
        if char not in delete:
            palindrome += char
    
    return palindrome, palindrome == palindrome[::-1]