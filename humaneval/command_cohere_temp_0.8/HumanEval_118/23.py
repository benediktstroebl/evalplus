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

The Python script defines a function `get_closest_vowel` that takes in a word as an input. It counts the number of consecutive consonants from the right side of the word, excluding the vowels in the beginning and ending. If there are consonants, it searches for the next closest vowel in the word that is between two consonants, and returns it. If no such vowel is found, it returns an empty string. 

The script assumes that the given word contains only English letters. You can test this script using the examples provided in the problem statement to see if it passes. Feel free to modify the test cases to include other scenarios.