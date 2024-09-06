def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """ Returns the shortest palindrome string that starts with the input string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix in the input string
    index = len(string) - len(string)[::-1].index(string[::-1])
    # Reverse the part before the palindrome suffix and append it to the input string
    return make_palindrome(string[:index] + string[index:][::-1])