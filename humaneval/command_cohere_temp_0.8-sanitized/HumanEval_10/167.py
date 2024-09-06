def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.find_reverse(string, 0, len(string) // 2)
    palindromic_suffix = string[i:]

    # Reverse the prefix up to the palindromic suffix.
    new_string = string[:i] + palindromic_suffix[::-1]

    # Return the shortest palindrome.
    if len(new_string) > len(string):
        return make_palindrome(new_string)
    else:
        return new_string