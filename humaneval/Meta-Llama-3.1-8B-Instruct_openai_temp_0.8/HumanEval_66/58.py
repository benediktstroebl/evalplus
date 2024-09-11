```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the ASCII codes of its upper characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the upper characters in the string.
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

This script defines a function `digitSum` that uses a generator expression to iterate over the characters `c` in the input string `s`. The `ord(c)` function returns the ASCII code of the character, and the `if c.isupper()` condition ensures that only upper case characters are included in the sum. The `sum` function then adds up the ASCII codes of the upper case characters. The example usage at the end demonstrates the function's behavior with the given test cases.