```python
def digitSum(s):
    """Returns the sum of the ASCII codes of the upper characters in the input string."""
    
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # If uppercase, add its ASCII code to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Example usage:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper characters. It uses a simple loop to iterate over each character in the string, checks if it's uppercase using the `isupper` method, and adds its ASCII code to the total sum if it is. The total sum is then returned.