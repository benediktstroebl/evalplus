def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])

    # Reverse the prefix before the palindromic suffix
    prefix = string[:i] + string[i:i+1][::-1]

    return prefix + string[i+1:]