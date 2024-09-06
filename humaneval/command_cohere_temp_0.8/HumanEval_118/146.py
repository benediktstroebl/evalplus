```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Convert the word to lowercase to make the comparison case insensitive
    word = word.lower()
    
    # Split the word into individual characters and initialize the previous consonant and current vowel variables
    word = list(word)
    prev_consonant = True
    current_vowel = ''
    
    for char in word:
        if char in vowels:
            if not prev_consonant:
                current_vowel = char
        elif char in consonants:
            prev_consonant = True
        else:
            # If the character is not a consonant or a vowel, it is not taken into account for the closest vowel computation
            continue
    
    # If the above loop completes without setting a valid current_vowel, return an empty string
    if not current_vowel:
        return ''
    
    # If the end of the word is reached and there is no consonant after the current vowel, it is the closest vowel
    if not prev_consonant:
        return current_vowel
    
    # If the above conditions are not met, the closest vowel is the first vowel encountered after the last consonant
    return current_vowel
```

This script assumes only the English alphabet is included in the `word` parameter for simplicity. Additionally, it ignores any characters that are not consonants or vowels when determining the closest vowel. It iterates through the characters of the lowercase word, tracking the previous consonant and current vowel. The closest vowel is determined and returned, or an empty string if no qualifying vowel is found. 

Let's dive into each step of the process for further clarity:
1. **Lowercase Conversion**: The function converts the input word to lowercase with `word = word.lower()`. This ensures the comparison is case insensitive, making it adaptable to various letter variations.
2. **Word Splitting and Variable Initialization**: The function transforms the input word into a list of individual characters with `word = list(word)`. It then initializes two important variables:
   - `prev_consonant`: This boolean variable is set to `True` at the beginning since the rightmost side of the word is considered first. It indicates whether the previous character was a consonant.
   - `current_vowel`: This variable stores the vowel encountered, which is initially set to an empty string.
3. **Iterating Through Each Character**: The function iterates through each character in the list of characters (`word`) with a `for` loop. It checks if the character is a vowel or a consonant with the following logic:
   - If the character is a vowel (`char in vowels`), it further checks if the previous character was a consonant. If so, the `current_vowel` variable is updated to store this vowel character.
   - If the character is a consonant (`char in consonants`), the `prev_consonant` variable is updated to `True`.
   - If the character is neither a consonant nor a vowel, it is ignored from consideration for the closest vowel (`continue`). This includes digits, punctuation, and other non-alphabetic characters.
4. **Determining the Closest Vowel**: After iterating through all characters, the function determines the closest vowel based on the conditions outlined earlier. If the end of the word is reached and there was no consonant after the current vowel (`not prev_consonant`), this `current_vowel` is returned as the closest vowel. This ensures that any vowels at the