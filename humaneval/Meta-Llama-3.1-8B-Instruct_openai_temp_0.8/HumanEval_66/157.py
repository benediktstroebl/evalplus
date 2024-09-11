```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of all uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of uppercase characters.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Initialize sum as 0
    total_sum = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)

    # Return the total sum
    return total_sum

# Test the function with examples
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this code, we use a for loop to iterate over each character in the input string. We check if the character is uppercase using the `isupper()` method, and if it is, we add its ASCII code to the total sum using the `ord()` function. Finally, we return the total sum.