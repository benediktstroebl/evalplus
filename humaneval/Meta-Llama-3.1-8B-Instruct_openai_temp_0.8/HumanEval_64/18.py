```python
def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the string.
    The function is case-insensitive.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    s = s.lower()  # Convert the string to lowercase for case-insensitive counting
    vowels = 'aeiou'  # Define the set of vowels
    y_count = 1 if s[-1] == 'y' else 0  # Special case for 'y' at the end of the string

    # Count the occurrences of each vowel in the string, excluding the special case for 'y'
    count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

    return count + y_count  # Return the total count of vowels, including the special case for 'y'

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input, converts it to lowercase for case-insensitive counting, and then counts the occurrences of each vowel in the string. The special case for 'y' at the end of the string is handled separately. The function returns the total count of vowels, including the special case for 'y'.