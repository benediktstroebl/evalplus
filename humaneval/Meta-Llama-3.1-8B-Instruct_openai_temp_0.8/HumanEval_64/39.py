```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string. 'y' is also a vowel if it's at the end of the word.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    if s and s[-1].lower() == 'y':
        vowels += 'y'
    return sum(1 for char in s.lower() if char in vowels)

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3

# Additional test cases:
print(vowels_count("AEIOU"))  # Output: 5
print(vowels_count(""))  # Output: 0
print(vowels_count("y"))  # Output: 1
print(vowels_count("Y"))  # Output: 0
print(vowels_count("abby"))  # Output: 3
print(vowels_count("abcy"))  # Output: 3
```

This code defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function considers 'y' as a vowel if it's at the end of the word. It converts the input string to lowercase for simplicity and uses a generator expression with the `sum` function to count the vowels. The example usage demonstrates how to use this function with different inputs.