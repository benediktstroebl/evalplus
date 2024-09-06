def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome that begins with the supplied string """
    if is_palindrome(string):
        return string
    # Find the longest palindromic postfix
    palindromic_postfix_start = len(string) - len(string)[::-1].index(string)
    # palindromic_postfix = string[len(string) - palindromic_postfix_start - 1: len(string)]
    # Remove the palindromic postfix from the string and add it again at the beginning.
    # Then do the same thing after f'xchimp' (reverse of postfix)
    tmp = string[len(string) - palindromic_postfix_start: ]
    string = string[:len(string) - palindromic_postfix_start - 1] + tmp + tmp[::-1]
    return make_palindrome(string)