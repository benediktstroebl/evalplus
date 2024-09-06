```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), len(word))
    if index == 0 or index == len(word) or word[index-1:] == 'an' or word[index-1:] == 'en':
        return ''
    
    vowel = next((v for v in vowels if v in word[index-2:index]), '')
    
    return vowel
```

This script leverages Python's string manipulation capabilities and list comprehensions to find the closest vowel to the right of a consonant in the word. It checks if the vowel is in the beginning, ending, or already surrounded by a consonant and an additional consonant. If none of these conditions are met, an empty string is returned.  This approach provides a concise and efficient solution to the problem.