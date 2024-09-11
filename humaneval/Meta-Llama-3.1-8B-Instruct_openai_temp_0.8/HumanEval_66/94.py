```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(char) for char in s if char.isupper())

# Example usage:
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

Explanation:

- The function uses a generator expression to iterate over each character in the string `s`.
- The `isupper()` method checks if a character is an uppercase letter.
- The `ord()` function returns the ASCII code of a character.
- The `sum()` function calculates the sum of the ASCII codes of upper case characters.
- The example usage demonstrates how to call the function with different inputs and print the results.