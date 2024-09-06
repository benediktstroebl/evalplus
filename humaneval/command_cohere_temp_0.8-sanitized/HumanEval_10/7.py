def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Generate the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string + string[::-1]
    else:
        middle = len(string) // 2
        return make_palindrome(string[:middle]) + make_palindrome(string[middle:])