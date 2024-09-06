def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    index = 0
    palindrome = True
    for char in s:
        if char in delete:
            index += 1
        elif char in reverse:
            index -= 1
        if index < 0:
            palindrome = False
            break
    return (s[index:], palindrome)