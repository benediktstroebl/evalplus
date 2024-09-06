def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('^'+string[::-1])
    
    # Reverse the prefix before the palindromic suffix
    prefix = string[:i][::-1]

    # Construct the shortest palindrome
    return f"{string[i:]}{prefix}"