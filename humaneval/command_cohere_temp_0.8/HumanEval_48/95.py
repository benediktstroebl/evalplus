```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    text = text.lower()  # Convert to lowercase for case-insensitive comparison
    return text == text[::-1]
```

This script defines a function, `is_palindrome`, that takes a string text as input and returns `True` if the input is a palindrome (reads the same backward as forward), and `False` otherwise. The function first converts the input to lowercase to ensure that the comparison is case-insensitive. It then checks if the text is the same as its reversed version by using slicing (text[::-1]) to reverse the string. The function is tested with the provided test cases, and the output matches the expected values.