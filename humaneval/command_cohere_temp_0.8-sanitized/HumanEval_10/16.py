def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(reversed(string)))

    # If no palindromic suffix, simply return the string
    if i == -1:
        return string

    return string.replace(string[i:], '', 1)