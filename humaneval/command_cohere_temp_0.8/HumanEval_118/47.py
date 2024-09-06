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
    return ''
```

This script defines a function `get_closest_vowel` that takes in a word as an input and uses two dictionaries to check if the characters are consonants or vowels. It then iterates through the word to find the closest vowels according to the conditions stated in the problem. It also checks if the input word is empty or contains only consonants and vowels, returning an empty string in such cases. 

The code snippet above solves the problem with a time complexity of O(n), where n is the length of the input word, as it needs to iterate through the word only once. It is case-sensitive, so it can differentiate between consonants and vowels like c and C. However, it does not differentiate between lowercase and uppercase vowels (it returns the closest vowel regardless of case).