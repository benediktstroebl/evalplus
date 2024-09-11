```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, we use a generator expression inside the `sum` function to iterate over each character `c` in the string `s`. The `isupper` method checks if a character is uppercase, and the `ord` function returns the ASCII code of a character. If a character is uppercase, its ASCII code is added to the sum.