```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given word.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the word.

    Parameters:
    s (str): The input string representing a word.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Initialize a counter for vowels
    count = 0
    
    # Convert the string to lowercase to handle case-insensitivity
    s = s.lower()
    
    # Check each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the word
        if char in 'aeiou' or (char == 'y' and s.endswith(char)):
            # Increment the vowel counter
            count += 1
    
    # Return the total vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```