This is a self-contained Python function that creates a palindrome given a string:
```python
def is_palindrome(string):  
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    longest_palindrome = ""
    is_palindrome = False

    for char in string:
        if is_palindrome:
            if char == string[-1] and len(longest_palindrome) < len(string):
                longest_palindrome = longest_palindrome[:-::-1] + char
            else:
                longest_palindrome += char
        else:
            is_palindrome = True

    return longest_palindrome
```
This function uses a simple algorithm to first determine if the string is a palindrome and if not, appends the reverse of the string prefix to the end of the string. It is also keeps appending until it identifies the first non-palindrome character and then switches to appending the palindrome.