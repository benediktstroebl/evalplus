```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels 'a', 'e', 'i', 'o', 'u' are considered vowels, and 'y' is
    considered a vowel only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to handle case sensitivity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to track if 'y' is at the end of the word
    y_at_end = False
    
    # Check if the last character is 'y'
    if s and s[-1] == 'y':
        # Set the flag to True
        y_at_end = True
        # Remove the last character from the string
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the vowel count
            count += 1
    
    # If 'y' was at the end of the word, increment the vowel count
    if y_at_end:
        count += 1
    
    # Return the total vowel count
    return count

print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
```
The provided script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. It considers 'y' as a vowel only when it is at the end of the word. The function handles case sensitivity by converting the input string to lowercase. It also includes example use cases at the end of the script.