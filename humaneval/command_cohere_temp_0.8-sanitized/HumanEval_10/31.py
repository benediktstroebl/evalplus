def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    
    # Find the position of the longest palindromic suffix
    palindrome_suffix_start = string.rfind(string[::-1])
    if palindrome_suffix_start == -1:
        return string + string[0:]
    
    # Reverse the prefix before the palindromic suffix and concatenate
    return string[:palindrome_suffix_start] + string[::-1][palindrome_suffix_start:]