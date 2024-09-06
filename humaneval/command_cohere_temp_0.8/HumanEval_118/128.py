```python
def get_closest_vowel(word):
    """
    Find the closest vowel to the right of consonant sequences within a word.
    
    Args:
        word (str): The input word.
    
    Returns:
        str: The closest vowel to the right of consonant sequences, or an empty string if none is found.
    """
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels and word[i] != word[len_word - 1]:
            right_side = word[i + 1:len_word]
            if any(c in consonants for consonants in consonant_sequences for c in right_side):
                return word[i]
        elif word[i] == word[len_word - 1]:
            break
    return ''
```

This code defines a function `get_closest_vowel()` that takes in a word as an input. It iterates through the word, checking if each character is a vowel and if it's not the last character. If it meets these conditions, it checks the characters to the right of the vowel to see if they form consonant sequences. If they do, the function returns the vowel; otherwise, it continues iterating through the word. Finally, if no valid vowels are found, it returns an empty string.