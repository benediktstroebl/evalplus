def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = len(string) - 1
    while i > 0 and string[i] == string[i - 1]:
        i -= 1

    # Reverse the prefix up to the palindromic suffix
    reversed_prefix = string[i:][::-1] + string[:i]
    return f"{reversed_prefix}{string[i:]}"