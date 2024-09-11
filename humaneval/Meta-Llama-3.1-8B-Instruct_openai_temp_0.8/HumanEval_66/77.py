```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the upper characters only ASCII codes.
    """
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test the function
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This Python script defines a function `digitSum` that takes a string `s` as input and returns the sum of the upper characters only ASCII codes. It uses a for loop to iterate over each character in the string, checks if the character is uppercase using the `isupper` method, and adds the ASCII code of the character to the total sum using the `ord` function. The test cases are included to demonstrate the function's correctness.