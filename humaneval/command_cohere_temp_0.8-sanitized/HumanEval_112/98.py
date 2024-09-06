def reverse_delete(s, c):
    delete = [char for char in c]
    palindrome = s[:]
    for i in range(len(s)):
        if s[i] in delete:
            palindrome = palindrome[:i] + palindrome[i+1:]
    return palindrome, palindrome == palindrome[::-1]