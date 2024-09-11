```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.
    """
    # Use a generator expression to iterate over each character in the string
    # The isupper() method checks if a character is uppercase
    # The ord() function returns the ASCII value of a character
    # The sum() function adds up all the ASCII values
    return sum(ord(c) for c in s if c.isupper())
```

You can test this function with the examples provided:

```python
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```