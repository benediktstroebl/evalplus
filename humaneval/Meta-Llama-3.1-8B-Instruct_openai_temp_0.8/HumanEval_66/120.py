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

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

In this script, we define a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string and checks if `c` is an uppercase character using the `isupper` method. If `c` is uppercase, it calculates its ASCII code using the `ord` function and sums them up. The result is then returned by the function. The test cases at the end of the script validate the correctness of the function.