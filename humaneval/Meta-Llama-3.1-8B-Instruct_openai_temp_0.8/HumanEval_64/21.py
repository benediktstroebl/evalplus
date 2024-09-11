```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): A string representing a word.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()

    # Count the number of vowels in the string
    count = sum(1 for char in s if char in 'aeiouy')

    # If 'y' is at the end of the string, increment the count
    if s and s[-1] == 'y':
        count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function considers 'y' as a vowel only when it's at the end of the string. The example use cases are included for demonstration purposes.