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

This `is_palindrome` function takes a string text as input and first converts it to lowercase and removes any non-alphanumeric characters using a list comprehension. Then, it checks if the reversed string matches the original string using slicing (`slicing ([::-1])` reverses a string). The function returns `True` if the input is a palindrome and `False` otherwise.

Here's how the function performs on the provided test cases:
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

This approach ensures that the function is self-contained without relying on external variables or configurations. It also maintains simplicity and efficiency in solving the 'Palindrome Detection' problem.