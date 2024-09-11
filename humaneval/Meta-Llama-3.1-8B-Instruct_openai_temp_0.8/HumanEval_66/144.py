```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.
    """
    # Initialize the sum to 0
    total_sum = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII value of the character to the total sum
            total_sum += ord(char)

    # Return the total sum
    return total_sum

# Test the function
print(digitSum(""))  # Should print 0
print(digitSum("abAB"))  # Should print 131
print(digitSum("abcCd"))  # Should print 67
print(digitSum("helloE"))  # Should print 69
print(digitSum("woArBld"))  # Should print 131
print(digitSum("aAaaaXa"))  # Should print 153
```

This script defines a function `digitSum` that calculates the sum of the ASCII codes of the upper case characters in a given string. It uses the `ord` function to get the ASCII value of each character and the `isupper` method to check if the character is upper case. The function then returns the total sum. The script also includes test cases to demonstrate the function's correctness.