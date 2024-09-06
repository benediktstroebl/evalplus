def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome that starts with the given string s."""
    if not s:
        return s

    # Find the position of the longest palindromic suffix.
    longest_palindrome_suffix_idx = len(s) - len(s)[::-1].find_longest_match(s, 0, len(s))

    # Extract the reverse of the shortest prefix that comes before the palindromic suffix.
    reversed_prefix = s[:longest_palindrome_suffix_idx][::-1]

    # Construct the shortest palindrome by concatenating the original string,
    # the reverse of the prefix, and the original palindromic suffix.
    return s + reversed_prefix + s[longest_palindrome_suffix_idx:]