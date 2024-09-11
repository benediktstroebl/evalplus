```python
def digitSum(s):
    """Returns the sum of the ASCII codes of the uppercase characters in the input string."""
    
    # Initialize the sum to 0
    ascii_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the sum
            ascii_sum += ord(char)
    
    # Return the sum
    return ascii_sum

# Test the function
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that takes a string as input and returns the sum of the ASCII codes of its uppercase characters. The function uses a loop to iterate over each character in the string, checking if it is uppercase using the `isupper` method. If the character is uppercase, its ASCII code is added to the sum using the `ord` function. Finally, the function returns the sum. The script also includes test cases to demonstrate the function's behavior.