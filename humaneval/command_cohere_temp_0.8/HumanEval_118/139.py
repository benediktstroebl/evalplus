```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Remove starting and ending vowels
    word = word.strip(vowels)
    
    if not word:
        return ""

    # Find the first vowel between two consonants from the right
    for i in range(len(word)-1):
        if word[i] not in consonants and word[i+1] not in consonants and word[i+1] in vowels:
            return word[i+1]
    else:
        return ""
```

This script utilizes Python's string methods to efficiently remove starting and ending vowels from the given word, preparing it for further processing. It then iterates through the word's characters from the right, checking for the presence of a consonant-vowel pattern. This approach ensures that the function correctly identifies the closest vowel standing between two consonants, as required by the problem statement.