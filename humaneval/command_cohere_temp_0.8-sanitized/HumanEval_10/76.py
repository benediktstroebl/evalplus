import re
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    palindrome = s + ''.join(re.findall(f'(.*)({s}[a-zA-Z]*){s}', s + s[::-1]))
    return palindrome