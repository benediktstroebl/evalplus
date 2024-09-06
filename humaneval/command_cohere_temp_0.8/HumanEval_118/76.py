```python
def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences in a string.
    
    Args:
        word (str): Input string.
    
    Returns:
        str: Closest vowel char to the right of consonant sequences or an empty string.
    """
    vowels = 'AEIOUaeiou'  
    # Convert to lowercase to handle case insensitivity
    word = word.lower()
    # Split the word into individual chars and initialize the flag
    chars = list(word)
    found = False

    # Iterate through each char in the word
    for i in range(len(chars)):
        char = chars[i]
        # If current char is a vowel and not the last char, move to the next iteration
        if char in vowels and i < len(chars) - 1:
            continue
        # If current char is a consonant and the next char is a vowel, set the flag true
        elif char not in vowels and i < len(chars) - 1 and chars[i+1] in vowels:
            found = True
        # If a consonant sequence is found and the flag is false, return an empty string
        elif char not in vowels and not found and i < len(chars)-1:
            return ''
        # Set the flag true whenever a vowel is encountered in a consonant sequence
        found = False
    # Return the last char if the flag is true, otherwise an empty string
    return chars[-1] if found else ''
```

This script provides a function `get_closest_vowel()` that takes in a string `word` as input and returns the closest vowel to the right of consonant sequences in the word. The function checks each character in the word, maintaining a flag that identifies consecutive consonant sequences. Whenever a vowel is encountered within such a sequence, the flag is marked as true, and the function returns the last character of the word if the flag is true; otherwise, it returns an empty string. The script efficiently solves the problem with a time complexity of O(n), where n is the length of the input word.