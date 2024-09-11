### Digit Sum Function
```python
def digitSum(s):
    """Returns the sum of the upper characters only in the input string's ASCII codes.

    Args:
    s (str): Input string

    Returns:
    int: Sum of upper characters' ASCII codes
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
This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper characters. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to filter out non-upper characters. The `sum` function is used to calculate the total sum. The test cases are then executed to verify the correctness of the function.