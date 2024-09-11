### Palindrome Check Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    return text == text[::-1]


# Example usage:
if __name__ == "__main__":
    test_cases = ["", "aba", "aaaaa", "zbcd"]
    for test_case in test_cases:
        result = is_palindrome(test_case)
        print(f"Is '{test_case}' a palindrome? {result}")
```

**Explanation:**

This script defines a function `is_palindrome` that takes a string `text` as input and returns `True` if the string is a palindrome and `False` otherwise.

The function uses Python's slicing feature `text[::-1]` to reverse the input string, and then checks if the reversed string is equal to the original string. If they are equal, the function returns `True`, indicating that the string is a palindrome.

The example usage section demonstrates how to use the `is_palindrome` function with a list of test cases. It prints the result of the palindrome check for each test case.

**Commit Message:**

`Added is_palindrome function to check if a given string is a palindrome.`