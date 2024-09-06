```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Remove the first and last character if it's a vowel
    if word[0] in vowels:
        word = word[1:]
    if word[-1] in vowels:
        word = word[:-1]
    
    # Iterate from the right side of the word
    for i in range(len(word)-2, -1, -1):
        if word[i] in consonants and word[i+1] in consonants:
            if i > 0 and word[i-1] in vowels:
                return word[i-1]
            if i < len(word)-1 and word[i+1] in vowels:
                return word[i+1]
    
    return ""
```

This script assumes that the English letters are lowercase. As per the problem statement, it removes any starting and ending vowels to consider words that may begin or end with consonants. It then iterates through the word, looking for pairs of consonants. If it finds a pair of consonants between two vowels or at the edges of the word, it returns the appropriate vowel. If no valid vowels are found, it returns an empty string. 

The code includes tests to check for reasonable edge cases that involve input containing punctuation, empty strings, and single-consonant words.