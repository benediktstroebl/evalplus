```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    vowels = 'aeiou'
    if s and s[-1].lower() == 'y':
        vowels += 'y'
    return sum(1 for char in s if char.lower() in vowels)

# Testing the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("helloy"))  # Expected output: 3
print(vowels_count("world"))   # Expected output: 1
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the count of vowels in the string. The function checks if the last character of the string is 'y' (ignoring case), and if so, it includes 'y' in the list of vowels. It then uses a generator expression to count the number of characters in the string that are vowels. The function is tested with several example inputs to demonstrate its correctness.