```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching the vowel
    """
    vowels = 'AEIOUaeiou'
    # Remove starting and ending vowels
    word = word.strip('AEIOUaeiou').strip('AEIOUaeiou')
    if len(word) < 2:
        return ''
    for i in range(1, len(word) - 1):
        if word[i] in vowels:
            if word[i - 1] in consonants and word[i + 1] in consonants:
                return word[i]
    return ''

# Define consonant characters
consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
```

This script defines a function `get_closest_vowel` that takes in a word as input. It removes starting and ending vowels to facilitate processing. It then iterates through the characters of the word, checking if the current character is a vowel and whether it is sandwiched by consonants. The function returns the first vowel that meets these conditions, or an empty string if no such vowel is found. 

The script ensures correctness and flexibility in handling different kinds of words through the removal of starting and ending vowels, and the use of both uppercase and lowercase vowel checks.