def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Reverse the prefix up to the palindromic suffix
    suffix = string[i:]
    prefix = string[:i]
    return string + prefix[::-1]