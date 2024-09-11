### Digit Sum Function
Here's a Python function that calculates the sum of ASCII codes of upper case characters in a given string.
```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example usage:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

Explanation:
- The `ord` function is used to get the ASCII value of a character.
- The `isupper` method is used to check if a character is an uppercase letter.
- The `sum` function is used to calculate the sum of ASCII values of upper case characters.
- The `for` loop is used to iterate over each character in the string, and the `if` condition is used to filter out non-upper case characters.