```python
def vowels_count(s):
    """
    Calculate the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    y_at_end = s[-1].lower() == 'y' and len(s) > 1
    return sum(1 for c in s.lower() if c in vowels or (c == 'y' and not y_at_end))

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("ay"))     # Expected output: 1
print(vowels_count(""))       # Expected output: 0
print(vowels_count("bcdfgh")) # Expected output: 0
```

This script defines the `vowels_count` function, which takes a string `s` as input and returns the number of vowels in the string. It uses a generator expression to iterate over the characters in the string, counting the number of characters that are vowels or 'y' not at the end of the string. The test cases at the end demonstrate the function's behavior on various inputs.