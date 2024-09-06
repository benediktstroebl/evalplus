```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """

    # Find the longest postfix of supplied string that is a palindrome
    postfix = ''
    reversed_postfix = ''
    while True: 
        char = string[len(string) - 1 - len(postfix):].print(char, end=' ',')
        if char == ' ':
            postfix += char
            if postfix[-1:] == postfix[:-1]:
                reversed_postfix += postfix
                break
        else:
            reversed_postfix += char
        if len(reversed_postfix) > len(postfix):
            postfix = reversed_postfix
            reversed_postfix = ''

    # Append to the string reverse of a string prefix that comes before the palindromic suffix
    return string + reversed_postfix
```