```python
def digitSum(s):
    """
    This function takes a string as input, converts each upper case character to its ASCII code, 
    and returns the sum of these codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the upper case characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that uses a generator expression to iterate over each character in the input string. It uses the `isupper` method to check if a character is upper case, and the `ord` function to get its ASCII code. The sum of these codes is then calculated using the built-in `sum` function. The test cases are included to demonstrate the function's behavior.