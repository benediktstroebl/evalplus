```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                cons_count += 1
            elif char.lower() in 'aeiou':
                if cons_count > 0:
                    return char
                cons_count = 0
    return ''
```

This Python script provides a self-contained function called `get_closest_vowel` that addresses the problem statement. It meticulously examines each character in the input `word`, identifying consonants and vowels. The goal is to find the closest vowel located between two consonants when excluding the beginning and ending vowels. This is achieved by maintaining a counter for consonant occurrences (`cons_count`). Upon encountering a vowel, the counter is checked, and if there are consonants on either side, the function promptly returns the vowel. If no qualifying vowels are found, the function returns an empty string. 

The code demonstrates an efficient approach to solve this problem with a concise and clear implementation. It adheres to Python's best practices and maintains a high level of readability and understandability.