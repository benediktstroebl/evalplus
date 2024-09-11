```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper case characters. It uses a generator expression to iterate over each character in the string, checks if the character is upper case using the `isupper` method, and if so, adds its ASCII code to the sum using the `ord` function. The script also includes test cases to verify the correctness of the function.