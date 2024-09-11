```python
def digitSum(s):
    """Returns the sum of the upper characters only ASCII codes in the input string."""
    
    # Use a generator expression within the built-in sum function to add up the ASCII values of uppercase characters
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses the `ord()` function to get the ASCII value of each character, and the `isupper()` method to filter out non-upper case characters. The result is then summed up using the `sum()` function.