### Vowels Count Function
```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to make the counting case-insensitive
    s = s.lower()
    
    # Initialize the count of vowels
    count = 0
    
    # Check if the last character is 'y' and adjust the count accordingly
    if s and s[-1] == 'y':
        # If 'y' is at the end, consider it a vowel
        count += 1
        # Remove the last character from the string
        s = s[:-1]
    
    # Count the occurrences of 'a', 'e', 'i', 'o', 'u' in the string
    for char in s:
        if char in 'aeiou':
            count += 1
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello world"))  # Expected output: 3
print(vowels_count("y"))  # Expected output: 1
print(vowels_count(""))  # Expected output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It considers 'y' a vowel only if it's at the end of the string. The function is tested with several test cases to demonstrate its correctness.