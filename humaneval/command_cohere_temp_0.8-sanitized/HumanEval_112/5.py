def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:0]  # Create a new string with the same value as s (using s[:0] to create a new string with the same values but different reference)
    for i, char in enumerate(s):
        if char not in delete:
            palindrome += char
    return palindrome, palindrome == palindrome[::-1]