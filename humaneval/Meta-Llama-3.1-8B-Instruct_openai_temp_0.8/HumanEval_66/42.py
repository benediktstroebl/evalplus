```markdown
## Digit Sum Function

### Problem Description

This script calculates the sum of the ASCII codes of upper case characters in a given string.

### Code

```python
def digitSum(s):
    """
    Returns the sum of the upper case characters' ASCII codes in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper case characters' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example usage:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

### Explanation

The `digitSum` function uses a generator expression within the built-in `sum` function to calculate the sum of the ASCII codes of the upper case characters in the input string `s`. The `ord` function returns the ASCII code of a character, and the `isupper` method checks if a character is upper case.