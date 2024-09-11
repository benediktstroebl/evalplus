```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper case characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script uses a generator expression within the built-in `sum` function to calculate the sum of ASCII codes of upper case characters in the string. The `ord` function is used to get the ASCII value of each character, and `isupper` is used to check if the character is upper case.