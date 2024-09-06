def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix in the string
    palindromic_suffix_start = string.rfind(string[::-1])
    if palindromic_suffix_start == -1:
        return string + string[0:]

    # Find the length of the palindromic suffix
    palindromic_suffix_len = len(string) - palindromic_suffix_start - 1

    # Extract the reverse of the prefix up to the palindromic suffix
    prefix_to_suffix = string[:palindromic_suffix_start]
    reverse_prefix = prefix_to_suffix[::-1]

    # Append the reverse prefix to the string to create a palindrome
    return string + reverse_prefix