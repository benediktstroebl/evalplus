def reverse_delete(s, c):
    if not isinstance(s, str) or not isinstance(c, str):
        raise ValueError("Input must be strings!")
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome
s = "abcdedcba"
c = "ab"