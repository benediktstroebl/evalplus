def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix
    palindrome_suffix_start = len(string) - len(string)[::-1].index(string)
    # Reverse the prefix up to the palindrome suffix
    new_string = string[:palindrome_suffix_start] + string[::-1][palindrome_suffix_start:]
    # Return the new string if it is a palindrome, or revert to the original string
    if is_palindrome(new_string):
        return new_string
    else:
        return string