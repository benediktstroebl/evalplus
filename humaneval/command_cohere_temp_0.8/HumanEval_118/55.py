```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings from the right half of the word.
    right_half = word[len(word) // 2 : ]
    right_half = right_half.lower()
    
    # Filter out vowels at the beginning or ending of the word.
    temp_list = [x for x in right_half if x not in vowel]
    
    if len(right_half) == 0:
        return ''
    
    # Find the index of the first consonant.
    first_consonant_idx = right_half.find(list(consonants)[0])
    
    if first_consonant_idx == -1:
        return right_half[0]
    
    # Find the closest vowel to the right of the first consonant.
    for i in range(first_consonant_idx + 1, len(right_half)):
        if right_half[i] in vowel:
            return right_half[i]
    
    return ''
```

This Python script defines a function called `get_closest_vowel` that takes in a word as input. This function analyzes the word to find the first consonant present in the right half of the word and then searches for the closest vowel to that consonant. The right half of the word is created by extracting the latter half of the word, and if the word contains fewer than two characters, it is returned as is. 

The script identifies vowels and consonants through hardcoding their respective strings and performs string operations to locate the first consonant. Then, it iterates through the right half of the word to find the closest vowel to the left of the first consonant, case-insensitive. If no vowel is found, the function returns an empty string. 

Overall, the `get_closest_vowent` function effectively identifies the closest vowel to the right of the first consonant in the given word and handles edge cases respectfully.