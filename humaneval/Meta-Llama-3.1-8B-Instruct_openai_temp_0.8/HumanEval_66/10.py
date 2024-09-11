```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' 
    ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only' ASCII codes.
    """
    # Initialize the sum variable to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # If it is, add its ASCII code to the total sum
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

This script defines the `digitSum` function, which takes a string `s` as input, initializes a `total_sum` variable to 0, and then iterates over each character in the string. If a character is an uppercase letter (checked using the `isupper` method), its ASCII code is added to `total_sum` using the `ord` function. Finally, the function returns `total_sum`. The test cases at the end demonstrate the function's correctness.