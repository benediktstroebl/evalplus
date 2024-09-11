### Vowels Count Function
```python
# Define a string of vowels and a string of characters that are vowels at the end of the word
VOWELS = 'aeiouAEIOU'
END_VOWEL = 'yY'

def vowels_count(s):
    """
    Counts the number of vowels in a given word.
    
    A 'y' is considered a vowel only when it is at the end of the given word.
    
    Parameters:
    s (str): A string representing a word.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character of the word is a vowel
    if s and s[-1] in END_VOWEL:
        # If it is, decrement the count since 'y' is a vowel at the end
        count = 1
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in VOWELS:
            # If it is, increment the count
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```