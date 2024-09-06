Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    # Check if text is equal to its reverse
    return text == text[::-1]
```
This function first cleans the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then, it compares the cleaned string with its reverse using slicing to check if it's a palindrome. The function returns True if the text is a palindrome and False otherwise. The markdown code block with the function passes the given tests.