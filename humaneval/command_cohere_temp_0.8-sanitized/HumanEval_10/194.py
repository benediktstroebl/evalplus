def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # find the longest palindromic suffix
    i = string.rfind(string[::-1]) + 1
    
    # reverse the prefix up to the palindromic suffix
    new_string = string[:i] + string[i:i+1][::-1] + string[i+1:]
    return new_string