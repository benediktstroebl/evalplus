```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    index = len(word) - 1
    while index >= 0 and word[index] in consonants:
        index -= 1
    if index == -1:
        return ''
    left_consonant = word[index]
    right_consonant = word[index + 1]
    for vowel in vowels:
        if vowel == left_consonant or vowel == right_consonant:
            return vowel
    return vowels[vowels.find(left_consonant) // 2 + vowels.find(right_consonant) // 2]
```

The problem is solved using a Python script with a self-contained function `get_closest_vowel(word)` that takes a word as input and returns the closest vowel to the right side of the word, between two consonants. Case sensitivity is considered.

To determine the closest vowel, the function checks the last character of the word to see if it's a consonant. If it is, the function moves the index to the rightmost consonant in the word (assuming it's not the only consonant in the word). Then, based on the proximity of the adjacent consonants and vowels, it determines the closest vowel. The function returns an empty string if there are no vowels between the consonants.

This approach ensures that the function considers both uppercase and lowercase vowels and provides a straightforward solution to the problem.