def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the index of the longest palindromic suffix
    palindrome_suffix_idx = len(string) - len(string)[-1::-1].index(True)

    # Extract the reverse of the prefix before the palindromic suffix
    prefix_reverse = string[:palindrome_suffix_idx][::-1]

    # Construct the shortest palindrome by concatenating the original string and the reverse of the prefix
    shortest_palindrome = string + prefix_reverse

    return shortest_palindrome