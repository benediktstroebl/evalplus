```python
def digitSum(s):
    """
    This function takes a string as input, converts each character to its ASCII value, 
    filters out non-digit characters, and returns the sum of the remaining ASCII values.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII values of the upper case characters in the string.
    """
    # Initialize sum to 0
    total_sum = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert the character to its ASCII value and add it to the sum
            total_sum += ord(char)

    # Return the sum of the ASCII values of the upper case characters
    return total_sum

# Example usages:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input, calculates the sum of the ASCII values of the upper case characters in the string, and returns the sum. The example usages at the end demonstrate the function's behavior with various inputs.