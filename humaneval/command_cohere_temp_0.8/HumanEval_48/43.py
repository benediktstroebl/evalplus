Here's a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
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
This function uses a few tricks to make the palindrome check more efficient and robust. First, it converts the input text to lowercase and removes all non-alphanumeric characters using a list comprehension. This ensures that the palindrome check ignores spaces, punctuation, and other non-alphanumeric characters. Then, it compares the original text with its reverse using slicing, which is a more efficient way to reverse a string in Python. The result is a clean and reusable function that accurately determines whether a string is a palindrome.