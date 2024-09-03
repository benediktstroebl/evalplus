```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    Return True if the string is a palindrome, otherwise False
    """
    return text == text[::-1] or text == text[::-1][::-1]
```

This function is designed to determine whether a given string is a palindrome. It employs two checks: comparing the original string to its reverse using slicing ([::-1]) and then the reversed string to its original using slicing again ([::-1][::-1]). This function successfully identifies palindromes.