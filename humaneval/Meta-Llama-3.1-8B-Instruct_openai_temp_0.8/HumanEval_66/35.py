```markdown
### Code
```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

### Explanation

*   The `digitSum` function takes a string `s` as input and uses a generator expression to iterate over each character `c` in the string.
*   The `isupper` method checks if the character is an uppercase letter.
*   The `ord` function returns the ASCII code of a character.
*   The `sum` function calculates the sum of the ASCII codes of all uppercase characters in the string.
*   The test cases at the end of the script demonstrate the function's correctness.