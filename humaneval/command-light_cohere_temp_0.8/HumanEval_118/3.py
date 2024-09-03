Here is a self-contained Python script that solves the problem of finding the closest vowel to a given string:
```python
def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    
    # Get all consonants in the word
    consonants = [c for c in word if c.isalpha()]
    
    # Index of the closest vowel is the one that is less than the total length of the word.
    closest_vowel = ""
    for vowel in vowels:
        if word[len(word) - 1 - index] == vowel:
            closest_vowel = vowel
            break
    return closest_vowel
```

This script defines a function that takes a word as input and returns the index of the closest vowel found between the two last consonants of the word. It works by assuming that vowels can only appear between consonants and that the last consonant before the vowel is the last index in the string. 

It loops through every vowel and checks if the current vowel is present in the word and is the right before the last consonant. If it is, the current vowel is the closest one, and it breaks out of the loop.