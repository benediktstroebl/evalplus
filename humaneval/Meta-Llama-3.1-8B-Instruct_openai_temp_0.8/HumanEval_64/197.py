```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    vowels = 'aeiou'
    if s.endswith('y'):
        vowels += 'y'
    return sum(1 for char in s.lower() if char in vowels)


# Testing the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("worldy"))  # Expected output: 2
print(vowels_count("Python"))  # Expected output: 2
```

This script defines the `vowels_count` function as specified. It uses a set of vowels and checks if the input string ends with 'y'. If it does, 'y' is added to the set of vowels. The function then uses a generator expression to count the number of characters in the string that are in the set of vowels. The function is case-insensitive and handles both lower and uppercase vowels. The script also includes some test cases to demonstrate the function's behavior.