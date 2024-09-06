```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    index = len(word) - 1
    while index >= 0 and word[index] in consonants:
        index -= 1
    if index == -1:
        return ''
    vowel = word[index]
    if vowel in vowels:
        return vowel
    return get_closest_vowel(word[:index] + word[index + 1:])
```

This script defines a function called `get_closest_vowel` taking a single argument `word`, which attempts to find the closest vowel to a pair of consonants from the right side of the word. The script analyses the word and extracts the closest vowel to the pair of consonants. The function first identifies the index of the last consonant in the word. The consonant is then checked if it is a vowel, if it is, the function returns it. If it is not, the function recursively calls itself with the part of the word before and after the consonant.

This problem can be solved in many different ways, this solution's methodology is trying to attach the vowel to the right side of the word until a valid vowel is found.