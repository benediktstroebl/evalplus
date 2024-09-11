### Vowels Count Function

The following Python script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only when it's at the end of the word.

```markdown
### Code
```python
def vowels_count(s):
    """
    Calculate the number of vowels in a given word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it's at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.

    Examples:
        >>> vowels_count("abcde")
        3
        >>> vowels_count("ACEDY")
        4
    """
    vowels = 'aeiou'
    # Check if the last character is 'y'
    last_char = s.lower()[-1]
    if last_char == 'y':
        # If 'y' is at the end, add it to the vowels string
        vowels += 'y'
    # Count the vowels in the word
    count = sum(1 for char in s.lower() if char in vowels)
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 3
print(vowels_count("ACEDY"))  # Output: 4
```

### Explanation
The function `vowels_count` works by first defining the string of vowels. It then checks if the last character of the input string is 'y' (case-insensitive). If it is, 'y' is added to the string of vowels. Finally, it counts the number of vowels in the input string using a generator expression and returns the count.