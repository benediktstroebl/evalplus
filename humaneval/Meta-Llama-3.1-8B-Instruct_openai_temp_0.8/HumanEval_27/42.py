```markdown
### Flipping Case of a String

Below is a Python script that solves the problem using a simple one-liner and a more explicit solution:

```python
def flip_case_simple(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_simple('Hello')
    'hELLO'
    """
    return string.swapcase()

def flip_case_explicit(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_explicit('Hello')
    'hELLO'
    """
    return ''.join('' if char.isupper() else char.upper() if char.isalpha() else char for char in string)

# Example usage:
if __name__ == "__main__":
    test_string = "Hello World!"
    print("Original string:", test_string)
    print("Flipped case (simple):", flip_case_simple(test_string))
    print("Flipped case (explicit):", flip_case_explicit(test_string))
```

### Explanation:

- The `swapcase()` method in Python is used to swap the case of a string, effectively flipping the case of the original string.
- The second solution uses a more explicit approach, iterating over each character in the string. It checks if the character is a letter (using `isalpha()`), and if so, it swaps its case using `upper()` and `lower()`. Non-letter characters are left unchanged. The resulting characters are then joined back into a string using `''.join()`.