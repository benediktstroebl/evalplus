Here's a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed string matches the original string
    return text == text[::-1]
```

This `is_palindrome` function takes a string text as input and first converts it to lowercase and removes all non-alphanumeric characters using a list comprehension. Then, it checks if the reversed string matches the original string using slicing notation (`text[::-1]`) to reverse the string. It returns True if it's a palindrome and False otherwise.

To see it in action, let's run the function with a few test cases:
```python
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
```

This script ensures the function is self-contained and can be easily reused in other projects for checking palindromes without relying on any external variables or configurations. Feel free to adapt this code to your needs. If you have more questions or need further assistance, please don't hesitate to ask!