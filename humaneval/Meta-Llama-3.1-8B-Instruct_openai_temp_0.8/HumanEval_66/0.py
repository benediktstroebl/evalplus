```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only ASCII codes.
    """
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

In this script, the `digitSum` function uses a generator expression inside the `sum` function to iterate over the characters in the string `s`. It uses the `ord` function to get the ASCII code of each character and the `isupper` method to filter out the upper case characters. The `sum` function then adds up all these ASCII codes to return the result.