### Vowels Count Function
```python
# Define a string of vowels
VOWELS = 'aeiouy'

def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    'y' is considered a vowel only when it is at the end of the given word.
    The function is case-insensitive.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Initialize count of vowels
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in VOWELS:
            # If the character is 'y' and it's at the end of the string, increment count
            if char == 'y' and i == len(s) - 1:
                count += 1
            # Otherwise, increment count
            else:
                count += 1
    
    # Return the count of vowels
    return count

# Example use cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("aey"))    # Output: 3
```