Here's a Python script with a self-contained function that solves the problem of checking if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    
    Args:
        text (str): Text to be checked.
        
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```
This script defines a function 'is_palindrome' that takes a string text as an argument and returns 'True' if the text is a palindrome (reads the same backwards as forwards), and 'False' otherwise.

The logic is to first clean the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then, it compares the cleaned string with its reverse using slicing ('text[::-1]') to determine if it's a palindrome.