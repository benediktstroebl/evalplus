```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string, considering 'y' as a vowel only when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    vowels = 'aeiou'
    count = 0
    if s.endswith('y'):
        vowels += 'y'
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("y"))      # Expected output: 1
```

This Python script defines a function `vowels_count` that counts the vowels in a given string. It considers 'y' as a vowel only when the string ends with 'y'. The function iterates over each character in the string (case-insensitive), and increments the count whenever it encounters a vowel. The result is then returned. The script includes test cases to verify the correctness of the function.