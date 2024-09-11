```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example use cases:
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

In this script, we use the `ord` function to get the ASCII code of each character, and the `isupper` method to filter out the lower case characters. The `sum` function is then used to calculate the total sum of the ASCII codes.