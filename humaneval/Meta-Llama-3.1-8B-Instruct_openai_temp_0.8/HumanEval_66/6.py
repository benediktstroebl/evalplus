```markdown
### Digit Sum Function

#### Problem Description

Write a function that takes a string as input and returns the sum of the upper characters only' ASCII codes.

#### Solution

```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string

    Returns:
        int: The sum of ASCII codes of upper characters
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

#### Explanation

*   We use the `ord()` function to get the ASCII code of each character in the string.
*   We use the `isupper()` method to check if a character is an uppercase letter.
*   We iterate over each character in the string, check if it's an uppercase letter, and add its ASCII code to the total sum if it is.
*   Finally, we return the total sum.