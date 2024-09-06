Here's a Python script that contains a function named `count_upper()` which solves the problem as per the provided Markdown code block:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # List of uppercase vowels
    vowels = 'AEIOU'
    
    # Initialize count
    count = 0
    
    # Iterate through the string
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in vowels and s[i].isupper():
            count += 1
    
    return count

# Sample Tests
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0
```

This script includes the function `count_upper()`, which takes a string as its input and returns the number of uppercase vowels in even indices of the string. The function checks if each character at an even index is an uppercase vowel, and increment the count if it is. The script then applies this function to test cases and outputs the expected results.