```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # Should print: 0
print(digitSum("abAB"))  # Should print: 131
print(digitSum("abcCd"))  # Should print: 67
print(digitSum("helloE"))  # Should print: 69
print(digitSum("woArBld"))  # Should print: 131
print(digitSum("aAaaaXa"))  # Should print: 153
```

In this script, we define a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper case characters. The function iterates over each character in the string, checks if it's an upper case letter using the `isupper` method, and if so, adds its ASCII code (obtained using the `ord` function) to the total sum. Finally, the function returns the total sum. We also include test cases at the end of the script to verify that the function works correctly.