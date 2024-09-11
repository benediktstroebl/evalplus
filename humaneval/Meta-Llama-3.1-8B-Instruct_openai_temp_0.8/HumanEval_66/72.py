```python
def digitSum(s):
    """
    Returns the sum of the upper characters only ASCII codes in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only ASCII codes.
    """
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test the function with examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, we define a function `digitSum` that iterates over each character in the input string `s`. If the character is an uppercase letter (`isupper()` method), we add its ASCII code (`ord()` function) to the total sum. Finally, we return the total sum. The script includes test cases to demonstrate the function's correctness.