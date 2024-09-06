```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    word = word.upper()
    
    if word[0] in consonants and word[-1] in consonants:
        for i in range(1, len(word) - 1):
            if word[i] in vowels:
                return word[i]
        else:
            return ''
    else:
        return ''
```

This script contains a function `get_closest_vowel` that takes in a string `word` as input. It initially converts the word to uppercase to make the processing case-insensitive. It then checks if the word's first and last characters are consonants. If so, it iterates through the characters in the word's middle, checking if they are vowels. The function returns the closest vowel to the right, or an empty string if no qualifying vowels are found. 

The vowel and consonant strings are defined for case-insensitive processing and are optimized for English language characters, but they can be adjusted for different languages or cases as needed.