def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])

    # Return the shortest palindrome possible
    if i == 0:
        return string + string[::-1]
    return string[i+1:] + string[:i+1][::-1]