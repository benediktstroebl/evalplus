def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # find the position of the longest palindrome suffix
    palindrome_suffix_pos = len(s) - len(s)[::-1].find(s)

    # extract the palindrome suffix
    palindrome_suffix = s[-(palindrome_suffix_pos):]

    # walk backwards up to the palindrome suffix to find the shortest matching prefix
    prefix = s[:-(s[::-1].rfind(palindrome_suffix[:-1]))]
    
    # construct the return string by concatanating prefix and reverse of suffix
    return f"{prefix}{palindrome_suffix[::-1]}"