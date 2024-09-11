```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters.
    """
    # Use a generator expression within the sum function to iterate over each character in the string
    # The isupper method is used to check if a character is upper case, and the ord function to get its ASCII code
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this code:

*   We define a function `digitSum` that takes a string `s` as input.
*   We use a generator expression within the `sum` function to iterate over each character `c` in the string.
*   We use the `isupper` method to check if a character is upper case, and the `ord` function to get its ASCII code.
*   We return the sum of the ASCII codes of the upper case characters.
*   We test the function with the provided examples.