Here is a self-contained Python function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Check if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = []
    for char in string:
        if char == char[::-1]:
            longest_palindrome.append(char)
   
    if len(longest_palindrome) > 0:
        return longest_palindrome + longest_palindrome[::-1]
    else:
        return string
```
This function follows the idea of finding the longest postfix of the given string that is a palindrome, and then reversing the string prefix and appending it to the end of the string to create the palindrome.