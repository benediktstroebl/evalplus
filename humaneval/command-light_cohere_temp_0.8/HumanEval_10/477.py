```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    palindrome = ''
    reversed_prefix = string[::-1]
    while True:
        if reversed_prefix == reversed_prefix[::-1]:
            reversed_prefix = string[0:1]  # check for the first non-palindromic character
            if not string[1:]:
                break  # if the first non-palindromic is reached, append the current palindrome
        palindrome = palindrome + reversed_prefix
        reversed_prefix = string[0:1]  # check for the next non-palindromic character
    return palindrome
 ```