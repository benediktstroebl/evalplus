### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove whitespace and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```
In this script, we define a function `is_palindrome` that takes a string `text` as input and returns a boolean indicating whether the string is a palindrome.

Here's a step-by-step breakdown of the function:

1. We remove all whitespace characters and convert the string to lowercase using a generator expression with `isalnum()` and `lower()`.
2. We compare the cleaned string with its reverse using slicing (`[::-1]`).
3. If the cleaned string is the same when reversed, the original string is a palindrome, and we return `True`.

The example usage section demonstrates how to use the `is_palindrome` function with various input strings.