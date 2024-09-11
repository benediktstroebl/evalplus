```markdown
### Digit Sum Function

The following Python function calculates the sum of the ASCII codes of upper case characters in a given string.

#### Code

```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper case characters' ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper case characters' ASCII codes.
    """
    return sum(ord(char) for char in s if char.isupper())

# Example usage:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

#### Explanation

The function uses a generator expression to iterate over each character in the string. The `ord()` function is used to get the ASCII code of each character. The `isupper()` method is used to check if the character is an upper case letter. The `sum()` function is used to calculate the sum of the ASCII codes of the upper case characters.

This approach is efficient as it uses a generator expression, which avoids creating intermediate lists and uses less memory. The `ord()` function and `isupper()` method are also efficient as they are implemented in C and have low overhead.