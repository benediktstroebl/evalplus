def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string:
    i = len(string) - 1
    while i > 0 and string[i] == string[i+1]:
        i -= 1
    longest_palindromic_suffix = string[i+1:]

    # Find the longest non-palindromic prefix of the string:
    j = 0
    while string[j] == string[i+1]:
        j += 1
    longest_non_palindromic_prefix = string[:j]

    # Construct the shortest palindrome possible:
    new_string = longest_palindromic_suffix + longest_non_palindromic_prefix[::-1]

    # Return the new string if it's longer than the original, otherwise return the original:
    if len(new_string) > len(string):
        return new_string
    else:
        return string