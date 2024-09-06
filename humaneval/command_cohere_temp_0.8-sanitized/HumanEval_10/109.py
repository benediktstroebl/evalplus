def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindrome suffix
    i = string.rfind('.{}'.format(string[::-1]))
    palindrome_suffix = string[i:]

    # Remove the palindrome suffix from the string
    string = string[:i]

    # Reverse the string before the palindrome suffix and append
    return make_palindrome(string) + palindrome_suffix