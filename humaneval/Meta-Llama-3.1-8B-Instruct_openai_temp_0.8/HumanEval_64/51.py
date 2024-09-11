```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string, considering 'y' as a vowel when at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    if s.endswith('y'):
        vowels += 'y'
    return sum(1 for char in s.lower() if char in vowels)

# Example usage:
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel when it appears at the end of the word. The function uses a generator expression to count the number of vowels in the string. The `sum` function is then used to calculate the total count. The example usage at the end shows how to use the function with different inputs.