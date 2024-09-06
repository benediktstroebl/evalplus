def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.find_longest_match(string[::-1], 0, len(string) // 2)
    palindromic_suffix = string[i:]

    # Reverse a string prefix that comes before the palindromic suffix.
    prefix = string[:i]
    reversed_prefix = prefix[::-1]
    new_palindrome = palindromic_suffix + reversed_prefix

    return make_palindrome(new_palindrome)