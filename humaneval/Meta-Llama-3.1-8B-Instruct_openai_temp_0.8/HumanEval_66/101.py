```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII values of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example usage:
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that uses a generator expression to iterate over each character in the input string `s`. The `isupper()` method is used to filter out non-upper case characters, and the `ord()` function is used to get the ASCII value of each upper case character. The `sum()` function is then used to calculate the total sum of these ASCII values. The script also includes example usage at the end to demonstrate how to call the `digitSum` function with different inputs.