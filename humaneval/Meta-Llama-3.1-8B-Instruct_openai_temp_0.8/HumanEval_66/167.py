```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of ASCII codes of upper case characters only.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters in the input string.
    """
    # Initialize the sum variable to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII value of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a given string. It uses the `ord` function to get the ASCII value of each character and the `isupper` method to check if a character is upper case. The function iterates over each character in the string, sums up the ASCII values of upper case characters, and returns the total sum. The test cases at the end verify that the function works correctly.