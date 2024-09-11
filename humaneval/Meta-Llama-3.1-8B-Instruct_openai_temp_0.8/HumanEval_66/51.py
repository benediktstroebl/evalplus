### Solution
```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of upper characters.
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

### Explanation

*   We define a function `digitSum` that takes a string `s` as input.
*   We use a generator expression to iterate over each character `c` in the string.
*   We use the `isupper` method to check if the character is an uppercase letter. If it is, we calculate its ASCII code using the `ord` function.
*   We use the `sum` function to add up the ASCII codes of the uppercase characters.
*   The function returns the total sum.
*   We include test cases at the end to verify that the function works correctly.