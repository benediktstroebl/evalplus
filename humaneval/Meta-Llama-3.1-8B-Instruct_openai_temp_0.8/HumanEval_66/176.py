```python
def digitSum(s):
    """
    This function calculates the sum of the upper case ASCII codes in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper case ASCII codes in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, we define a function `digitSum` that uses a generator expression to iterate over each character `c` in the input string `s`. The `ord(c)` function returns the ASCII code of the character, and the `sum` function adds up these codes. The `if c.isupper()` part filters out the lower case characters.