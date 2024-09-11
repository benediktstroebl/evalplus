```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of the upper case characters in the input string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the ASCII codes of the upper case characters in the input string.
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

This script defines a function `digitSum` that calculates the sum of the ASCII codes of the upper case characters in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is upper case. The sum of the ASCII codes is calculated using a generator expression inside the `sum` function. The test cases are used to demonstrate the correctness of the function.