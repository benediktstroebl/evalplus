def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    palindrome = True
    for i in range(len(s)):
        if s[i] in delete:
            continue
        if reverse[i] != s[i]:
            palindrome = False
            break
    return (''.join(delete), palindrome)