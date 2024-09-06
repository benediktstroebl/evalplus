```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qwxz':
                cons_count += 1
        else:
            continue
    if cons_count > 1:
        if word[cons_count - 1].lower() in 'aeiou':
            return word[cons_count - 1]
    return ''
```

The problem requires finding the closest vowel that lies between two consonants from the right side of the word. The Python script defines a function `get_closest_vowel` that takes a word as input. It initially counts the number of consonants from the right side of the word. A consonant is defined as any letter that is not a vowel (case-sensitive) and excludes 'q', 'w', 'x', 'z' as well. 

If there is more than one consonant, it checks if the last character of the word (before the first consonant) is a vowel. If it is, this vowel is returned. If not, an empty string is returned, as there are no vowels between the last two consonants. This algorithm is straightforward and efficiently solves the problem. 

The code assumes that the given input is only English letters. The code is designed to efficiently solve the problem and is structured in a clear and understandable manner. It should be compatible with Python 3.x.