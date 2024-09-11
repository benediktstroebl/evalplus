```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper case characters.
    """
    # Initialize sum to 0
    total = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is upper case
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total += ord(char)
    
    # Return the total sum
    return total

# Test the function with examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of ASCII codes of upper case characters in the string. It uses a for loop to iterate over each character in the string, checks if the character is upper case using the `isupper()` method, and adds the ASCII code of the character to the sum if it is upper case. The total sum is then returned by the function. The script also includes test cases to demonstrate the function's correctness.