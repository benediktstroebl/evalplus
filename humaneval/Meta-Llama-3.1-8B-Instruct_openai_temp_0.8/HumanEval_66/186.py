```python
def digitSum(s):
    """
    This function takes a string as input, converts it to upper case, and returns the sum of the ASCII codes of the digits.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the digits in the string.
    """
    # Convert the string to upper case to handle both upper and lower case characters
    s = s.upper()
    
    # Initialize a variable to store the sum of ASCII codes
    ascii_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Add the ASCII code of the digit to the sum
            ascii_sum += ord(char)
    
    # Return the sum of ASCII codes
    return ascii_sum

# Test the function with the examples
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

In this script, the `digitSum` function takes a string as input, converts it to upper case using the `upper` method, and then iterates over each character in the string using a `for` loop. It checks if each character is a digit using the `isdigit` method, and if it is, it adds the ASCII code of the digit to a running sum using the `ord` function. Finally, it returns the sum of ASCII codes.