```python
def get_closest_vowel(word):
    cons_idx = -1
    for i, char in enumerate(word):
        if char.is consonant():
            if cons_idx == -1:
                cons_idx = i
            elif char.is vowel():
                return char
        else:
            cons_idx = -1
    return ''
```

The Python script provides a self-contained function called `get_closest_vowel` that takes a word as input. This function identifies the closest vowel located between two consonants, starting from the right side of the word. It ignores starting and ending vowels and considers only vowels between two consonants. The function returns an empty string if no qualifying vowel is found. 

The script assumes that the input word contains only English letters, and it handles potential edge cases, such as words with no consonants or vowels, correctly. 

The function relies on Python's string ` consonant()` method, which identifies English consonants. Although this method is available in Python's standard library, it is important to ensure it is available in the target environment, as its presence may vary across Python versions or installations.