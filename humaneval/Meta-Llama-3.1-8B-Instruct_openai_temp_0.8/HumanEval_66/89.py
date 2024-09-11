```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of the upper characters in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of the upper characters.
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