```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the upper characters only ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

In this script, we define a function `digitSum` that uses a generator expression to iterate over each character `c` in the input string `s`. The `isupper` method is used to determine if a character is an uppercase letter. If it is, the `ord` function is used to get its ASCII code, and this value is added to the sum. Finally, we print the results of the function for the provided test cases.