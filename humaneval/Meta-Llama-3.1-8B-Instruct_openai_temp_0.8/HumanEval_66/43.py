```markdown
### digitSum Function

#### Problem Description
Write a function that takes a string as input and returns the sum of the upper characters only' ASCII codes.

#### Code
```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of the upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of the upper case characters.

    Examples:
    >>> digitSum("")
    0
    >>> digitSum("abAB")
    131
    >>> digitSum("abcCd")
    67
    >>> digitSum("helloE")
    69
    >>> digitSum("woArBld")
    131
    >>> digitSum("aAaaaXa")
    153
    """
    return sum(ord(c) for c in s if c.isupper())
```

#### Explanation
This function uses a generator expression to iterate over each character in the input string. The `ord` function is used to get the ASCII code of each character. The `isupper` method is used to check if the character is upper case. If it is, its ASCII code is included in the sum. The `sum` function is used to calculate the total sum.
```