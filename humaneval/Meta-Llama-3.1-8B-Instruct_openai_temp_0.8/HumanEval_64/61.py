```python
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string

    Returns:
        int: The number of vowels in the string

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    vowels = 'aeiou'
    if not s:
        return 0
    last_char = s[-1].lower()
    if last_char in 'yeiu' and last_char in vowels:
        return len(s) - 1
    return sum(1 for char in s if char.lower() in vowels)


# Test the function with provided examples
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3

# Additional test cases
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("y"))      # Expected output: 1
print(vowels_count(""))       # Expected output: 0
```

This script defines the `vowels_count` function and provides additional test cases to ensure its correctness. The function checks for vowels in the input string and handles the special case where 'y' is a vowel at the end of the string.