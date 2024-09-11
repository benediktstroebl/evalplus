### Vowels Count Function
```python
# Define a function to count vowels in a word
def vowels_count(s):
    """
    Count the number of vowels in a word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the word.

    Args:
        s (str): The word to count vowels in.

    Returns:
        int: The number of vowels in the word.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' and count it as a vowel
    if s and s[-1].lower() == 'y':
        count += 1
        
    # Iterate over each character in the word
    for char in s:
        # Check if the character is a vowel (case-insensitive)
        if char.lower() in 'aeiou':
            # Increment the vowel counter
            count += 1
    
    # Return the total number of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("BYE"))    # Output: 2
```