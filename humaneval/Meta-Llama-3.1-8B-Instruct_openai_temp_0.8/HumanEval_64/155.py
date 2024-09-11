```python
# Define a function to check if a character is a vowel
def is_vowel(char):
    """Check if a character is a vowel.
    
    Parameters:
    char (str): The character to check.
    
    Returns:
    bool: True if the character is a vowel, False otherwise.
    """
    vowels = 'aeiou'
    # Check if the character is in the vowels string
    return char.lower() in vowels

# Define a function to count vowels in a word
def vowels_count(s):
    """Count the number of vowels in a word.
    
    Parameters:
    s (str): The word to count vowels in.
    
    Returns:
    int: The number of vowels in the word.
    """
    # Initialize a counter for vowels
    count = 0
    # Check if the last character is 'y' and if it's at the end of the word
    if len(s) > 1 and s[-1].lower() == 'y' and s[-2].isalpha():
        # If it is, consider it a vowel
        count += 1
    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel
        if is_vowel(char):
            # If it is, increment the counter
            count += 1
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("AEIOUY"))  # Output: 5
print(vowels_count("Hello World"))  # Output: 3
```

This script first defines a helper function `is_vowel` to check if a character is a vowel. The `vowels_count` function uses this helper function to count the number of vowels in a word. It also considers 'y' as a vowel if it's at the end of the word and its previous character is a letter. The script then tests the `vowels_count` function with some example cases.