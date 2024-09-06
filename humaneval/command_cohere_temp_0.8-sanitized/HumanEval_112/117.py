def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s == s[::-1]
    return ('', '') if not s else (s.translate(str.maketrans('', '', delete)), palindrome)