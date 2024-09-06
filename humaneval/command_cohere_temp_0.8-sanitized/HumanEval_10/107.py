def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]
def make_palindrome(string: str, ignored_char: str='') -> str:
    """ Generate shortest palindrome starting with string """
    if ignored_char:
        if not all(char in ignored_char for char in string):
            return ''

    # Corner cases
    if not string:
        return ''
    if is_palindrome(string):
        return string

    # Longest palindromic suffix
    i = string.rfind(string[::-1])
    if i == -1:
        return make_palindrome(string, string)

    # Everything after i is a palindrome
    palindromic_part = string[i+1:]
    non_palindromic_part = string[:i]

    # Extract reversed complementary non-palindromic part
    complementary = ''.join(reversed(non_palindromic_part))

    # Construct new palindrome by concatenating non-palindromic and complementary parts
    new_palindrome = f"{non_palindromic_part}{complementary}{palindromic_part}"
    return make_palindrome(new_palindrome, ignored_char)