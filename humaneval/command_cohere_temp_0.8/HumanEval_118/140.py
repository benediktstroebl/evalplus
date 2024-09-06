```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, char in enumerate(word) if char in consonants), len(word))
    if index == 0 or index == len(word) or word[index - 1:] == 'ea' or word[index + 1:] == 'ea':
        return ''
    else:
        return word[index].upper() if word[index] in vowels else ''
```

This script employs two dictionaries to determine the closest vowel in the word from the right side. The `consonants` dictionary stores all English consonants, and the `vowels` dictionary stores all English vowels. The algorithm first lowercases the input word to ensure case insensitivity. It then searches for the first consonant index using the `next()` function, with the help of the `consonants` dictionary.

If the consonant index is at the beginning or end of the word, or if the consonant is followed by 'ea', the function returns an empty string as it does not find any suitable vowels. Otherwise, it checks the vowel at the found consonant index, and returns it if it is a vowel. If not, it still returns an empty string, as the rule requires finding a vowel between two consonants from the right side of the word.