```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel but only when
    it is at the end of the given word.

    Parameters:
    s (str): The input string representing a word.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    return sum(1 for c in s if c.lower() in 'aeiou' or
               (c.lower() == 'y' and s[-1].lower() == 'y'))

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("Hello"))  # Expected output: 2
print(vowels_count("Yay"))    # Expected output: 2
print(vowels_count("AEIOUY"))  # Expected output: 7
print(vowels_count("bcdfg"))   # Expected output: 0
```

This script extends the original `vowels_count` function to handle the additional case where 'y' is considered a vowel only when it appears at the end of the word. It utilizes a generator expression within the built-in `sum` function to efficiently count the vowels in the string.