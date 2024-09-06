def is_palindrome(s):
    return s == s[::-1]
def make_palindrome(string):
    if not string:
        return string

    # find the longest palindrome suffix
    i = string.rfind(''.join(filter(is_palindrome, string)))
    if i == -1:
        return string

    # find the longest non-palindrome prefix
    j = string.rfind(''.join(filter(lambda c: not is_palindrome(c), string)))
    if j == -1:
        return string

    return make_palindrome(string[:j] + string[i:i+2][::-1] + string[j+1:])