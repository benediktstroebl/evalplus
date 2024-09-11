```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper case characters.
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

This script works by using a generator expression to iterate over each character `c` in the string `s`. The `isupper()` method checks if a character is an uppercase letter, and the `ord()` function returns the ASCII code of a character. The `sum()` function then adds up all these ASCII codes to give the final result.