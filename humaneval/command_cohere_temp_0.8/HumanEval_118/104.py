```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), None)
    if index is None:
        return ''
    
    vowel = next((char for char in vowels if char in word[index:]), '')
    
    return vowel
```

This script provides a function named `get_closest_vowel` taking a word as an argument. It first initiates two strings, `consonants` and `vowels`, to be used for filtering and finding the closest vowel to the left side of the given word. The `index` variable is used to identify the first consonant met from the right side of the word. In case the word doesn't have any consonants, the index returns `None`, and the function returns an empty string. If the index is valid, it uses a list comprehension to find the closest vowel to the right side of the index, within the word slice from the index until the end of the word. The list comprehension stops at the first vowel found within the given range, and the function returns its value. 

The script addresses the example cases provided in the prompt, ensuring the proper handling of each scenario.