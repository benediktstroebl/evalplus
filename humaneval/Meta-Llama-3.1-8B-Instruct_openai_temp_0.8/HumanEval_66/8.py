```python
def digitSum(s):
    """This function calculates the sum of ASCII codes of upper case characters in a string.
    
    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example usage
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script works by using a generator expression to iterate over each character `c` in the input string `s`. The `isupper()` method checks if a character is upper case. If it is, the `ord()` function returns its ASCII code. The `sum()` function then adds up all these ASCII codes.