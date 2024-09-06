def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(filter(str.ispalindrome, string)))

    # Extend the string with the reverse of the prefix
    new_string = string[i:i+1] + string[:i][::-1]
    return new_string