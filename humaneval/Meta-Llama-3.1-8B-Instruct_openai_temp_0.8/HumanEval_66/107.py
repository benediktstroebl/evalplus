### Digit Sum Function
#### A Python Function to Calculate the Sum of ASCII Codes of Uppercase Characters in a String

Below is a self-contained Python script that defines the function `digitSum` to calculate the sum of ASCII codes of uppercase characters in a given string.

```markdown
### Code
```python
def digitSum(s):
    """
    Calculates the sum of ASCII codes of uppercase characters in a string.

    Args:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of uppercase characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example use cases:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

### Explanation

1. The `ord(c)` function is used to get the ASCII code of each character `c` in the string.
2. The `isupper()` method is used to check if a character is uppercase. It returns `True` if the character is uppercase and `False` otherwise.
3. The `sum()` function is used to calculate the sum of ASCII codes of uppercase characters.
4. The generator expression `(ord(c) for c in s if c.isupper())` iterates over each character `c` in the string `s`, filters out lowercase characters using `c.isupper()`, and calculates the ASCII code of each remaining character using `ord(c)`.
5. The `sum()` function then adds up the ASCII codes of the uppercase characters to produce the final result.