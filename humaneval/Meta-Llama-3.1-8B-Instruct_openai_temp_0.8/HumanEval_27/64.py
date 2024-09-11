**Flipping Case in a String**
================================

Here is a Python script that defines the `flip_case` function as requested:
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```
Explanation:
In Python, the `swapcase()` string method returns a copy of the string where all uppercase characters are converted to lowercase and vice versa. We leverage this method to simplify the `flip_case` function.