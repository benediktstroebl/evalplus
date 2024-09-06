def is_palindrome(s):
    return s == s[::-1]
def make_palindrome(string):
    if not string:
        return string

    # find the longest palindromic suffix
    i = string.rfind(''.join(c for c in string if c == reversed(c)[0]))
    palindromic_suffix = string[i:]

    # if the whole string is a palindrome, return it
    if is_palindrome(string):
        return string

    # if no palindromic suffix, return original string
    if i == -1:
        return string

    # reverse the non-suffix to get the prefix
    prefix = string[:i] + reversed(string[i:])[1:]

    # construct the shortest palindrome
    return f"{prefix}{palindromic_suffix}"