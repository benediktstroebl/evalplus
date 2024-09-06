def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    
    # Extend the string with the reverse of the prefix before the palindromic suffix
    new_string = string[:i] + string[i:][::-1]
    
    # Return the new string if it's a palindrome, otherwise, repeat the process
    if is_palindrome(new_string):
        return new_string
    else:
        return make_palindrome(new_string)