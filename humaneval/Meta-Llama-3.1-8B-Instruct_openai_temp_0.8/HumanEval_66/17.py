### Digit Sum Function
```python
def digitSum(s):
    """
    Returns the sum of the upper characters only ASCII codes in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper characters only ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example use cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```
In this script:

1. The `digitSum` function uses a generator expression to iterate over each character `c` in the input string `s`.
2. The `isupper()` method checks if a character is uppercase. If it is, the `ord()` function returns its ASCII code.
3. The `sum` function adds up all the ASCII codes of the uppercase characters.
4. Example use cases demonstrate the function's behavior with different inputs.