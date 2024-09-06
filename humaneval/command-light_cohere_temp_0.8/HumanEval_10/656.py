```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    if not string:
        return ''
    string = ''.join(char for char in string if char == char[::-1] else char for char in string)
    return string + string[::-1][::-1]
```
The above code provides a function is_palindrome() which tests if a given string is a palindrome. Then the make_palindrome() function constructs a palindrome from a given string by iteratively selecting only the characters that are palindromes.