def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s == s[::-1]
    return (''.join(char for char in s if char not in delete), palindrome)