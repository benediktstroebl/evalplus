```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, char in enumerate(word) if char in consonants), len(word))
    return next((c for c in word[index:] if c in vowels), '')
```

The script uses two strings to initialize `consonants` and `vowels` to represent all English consonants and vowels respectively. The `index` variable is used to identify the first consonant from the right side of the given word. Initially, `index` is set to the length of the given word, then it's updated to the index of the first consonant from the right side of the word. Two successive consonants at the right side of the word lead to `index` being updated to the index of the second consonant. 

The script then checks the vowels after the consonant at the `index`, and returns the first match if found, or an empty string if no match is found. 

Overall, the solution is time-efficient with a time complexity of O(n) where n is the length of the input word. It's also space-efficient with a space complexity of O(1).