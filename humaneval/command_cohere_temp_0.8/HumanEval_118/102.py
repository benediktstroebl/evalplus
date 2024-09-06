```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    
    if len_word < 3:
        return ''

    # Find the first rightmost consonant
    for i in range(len_word):
        if word[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            rightmost_consonant_index = i
            break

    # Find the closest vowel to the rightmost consonant
    for i in range(rightmost_consonant_index + 1, len_word):
        if word[i] in vowels:
            return word[i]
    return ''
```

This script defines a function `get_closest_vowel` that takes in a word as an argument and returns the closest vowel to the right of the word, or an empty string if no eligible vowels are found. 

The script further highlights the following:
- A loop is used to identify the rightmost consonant of the word.
- It then iterates rightwards from this consonant to check for vowels, and returns the first one found. 

Overall, this solution is efficient with a time complexity of `O(n)` since it only iterates the list once and does not require any additional data structures.