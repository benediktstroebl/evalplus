```markdown
## Vowels Counter
### Python Function to Count Vowels in a Word

```python
def vowels_count(s):
    """
    Count the number of vowels in a word.

    Args:
    s (str): A string representing a word.

    Returns:
    int: The number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.
    """
    # Define vowels and special case for 'y' at the end of the word
    vowels = 'aeiouy'
    special_case = s[-1] == 'y'

    # Initialize count of vowels
    count = 0

    # Iterate over each character in the string
    for char in s:
        # Check if character is a vowel or 'y' in the special case
        if char.lower() in vowels or (char.lower() == 'y' and special_case):
            # Increment vowel count
            count += 1

    # Return total vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("apple"))  # Expected output: 2
print(vowels_count("yay"))    # Expected output: 2
print(vowels_count("y"))      # Expected output: 1
```

This Python script defines a function `vowels_count` to count the number of vowels in a word. Vowels are defined as 'a', 'e', 'i', 'o', 'u', but 'y' is also counted as a vowel if it appears at the end of the word. The function iterates over each character in the input string, checks if it's a vowel or 'y' in the special case, and increments a vowel count for each occurrence. The function returns the total vowel count.