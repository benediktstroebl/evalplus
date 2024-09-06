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
This function uses a combination of lowercase conversion and non-alphanumeric character removal to achieve the following:
- It converts the input string to lowercase to treat uppercase letters as equal to their lowercase counterparts.
- It removes all non-alphanumeric characters, leaving only letters and numbers. This step ensures that the function can handle oddball palindromes like 'aba' and 'aaaaa'.
- It then checks if the reversed string matches the original string, which is the defining characteristic of a palindrome.

To see how the function works with various test cases, you can call it with different input strings.