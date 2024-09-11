```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of uppercase characters.
    """
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that takes a string `s` as input, initializes a variable `total_sum` to 0, and then iterates over each character in the string. If a character is uppercase (checked using the `isupper()` method), its ASCII code (obtained using the `ord()` function) is added to `total_sum`. Finally, the function returns `total_sum`.