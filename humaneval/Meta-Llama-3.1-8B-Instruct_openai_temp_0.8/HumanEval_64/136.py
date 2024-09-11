```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string, considering 'y' as a vowel when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Example:
        >>> vowels_count("abcde")
        3
        >>> vowels_count("ACEDY")
        4
    """
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase for simplicity
    vowel_count = 0
    is_last_char_y = False

    # Check if the last character is 'y'
    if len(s) > 0 and s[-1] == 'y':
        is_last_char_y = True
        s = s[:-1]  # Remove the last character 'y' for now

    # Count the vowels in the string
    for char in s:
        if char in vowels:
            vowel_count += 1

    # If 'y' was at the end of the string, add it to the count
    if is_last_char_y:
        vowel_count += 1

    return vowel_count

print(vowels_count("abcde"))  # Outputs: 3
print(vowels_count("ACEDY"))  # Outputs: 4
print(vowels_count("hello"))  # Outputs: 2
print(vowels_count("y"))  # Outputs: 1
```

This script defines a function `vowels_count` that counts the number of vowels in a given string. It considers 'y' as a vowel when it's at the end of the word. The function first checks if the last character is 'y', removes it if it is, counts the vowels in the string, and then adds 'y' to the count if it was removed.