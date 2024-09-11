```python
def digitSum(s):
    """
    Returns the sum of the upper characters' ASCII codes in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters' ASCII codes.
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
Explanation:
- The function uses a generator expression to iterate over each character `c` in the input string `s`.
- The `isupper()` method is used to check if a character is upper case.
- If a character is upper case, its ASCII code is calculated using the `ord()` function and added to the sum.
- The `sum()` function is then used to calculate the total sum of the ASCII codes of the upper case characters.