```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of the uppercase characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the ASCII codes of the uppercase characters.
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

In this script, the `digitSum` function uses a generator expression to iterate over each character `c` in the input string `s`. The `ord(c)` function returns the ASCII code of `c`. The `isupper()` method is used to check if `c` is an uppercase letter. The `sum` function then adds up the ASCII codes of the uppercase characters.