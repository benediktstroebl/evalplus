def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])

    # Reverse the prefix up to the palindromic suffix
    new_string = string[:i] + string[i:][::-1]
    return new_string