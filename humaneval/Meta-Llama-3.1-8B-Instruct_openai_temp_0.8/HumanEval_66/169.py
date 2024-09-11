```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII values of uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII values of uppercase characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function with the provided examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, we define a function `digitSum` that takes a string `s` as input. We use a generator expression to iterate over the string, applying the `ord` function to each character to get its ASCII value, and the `isupper` method to check if the character is uppercase. We then use the `sum` function to add up these ASCII values. The result is returned by the function. Finally, we test the function with the provided examples.