def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome that begins with string """
    if not string:
        return string

    # Find the position of the longest palindromic suffix
    max_len, palindromic_suffix_pos = 0, 0
    for i, char in enumerate(string):
        if is_palindrome(string[-i-1:]):
            max_len, palindromic_suffix_pos = i + 1, i + 1

    # Extract the reverse of the prefix needed to make the string a palindrome
    required_prefix = string[:palindromic_suffix_pos][::-1]

    return make_palindrome(string[:palindromic_suffix_pos] + required_prefix)