```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, we define a function `digitSum` that uses a generator expression to iterate over each character `c` in the string `s`. The `ord` function returns the ASCII code of a character, and the `isupper` method checks if a character is uppercase. We use the `sum` function to add up the ASCII codes of the uppercase characters. Finally, we test the function with the examples provided.