```python
def digitSum(s):
    """Function to calculate the sum of ASCII codes of upper characters in a given string
    
    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper characters in the input string.
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

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper characters. The function uses a generator expression to iterate over the characters in the string, filtering out lower case characters using the `isupper` method. The `ord` function is used to get the ASCII code of each character, and the `sum` function is used to calculate the total sum.