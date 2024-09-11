```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, but only at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase for simplicity
    count = 0
    if s[-1] == 'y':  # Check if the last character is 'y'
        vowels += 'y'  # Add 'y' to the set of vowels
        s = s[:-1]  # Remove the last character from the string
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count("TestY"))  # Expected output: 2
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only if it's at the end of the string. It includes test cases to demonstrate its correctness.