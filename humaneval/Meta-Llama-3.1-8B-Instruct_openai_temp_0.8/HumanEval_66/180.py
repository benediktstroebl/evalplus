### Digit Sum Function
```python
def digitSum(s):
    """Returns the sum of the ASCII codes of upper characters in the input string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the ASCII codes of upper characters in the input string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example use cases:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```