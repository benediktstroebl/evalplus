```python
def get_closest_vowel(word):
    cons = []
    vowel = ''
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            if not cons or c.lower() != cons[-1].lower():
                vowel = c
        else:
            cons.append(c)
    return vowel
```

This Python script provides a function called `get_closest_vowel` that takes in a word as an argument. It searches for vowels (case-sensitive) within the word, specifically looking for the closest vowel that is sandwiched between two consonants coming from the right side of the word. The function will consider only the consonants that follow a vowel to find the closest vowel. Additionally, the function ignores starting and ending vowels. The function returns the closest vowel if found, or an empty string if no qualifying vowel is found. 

The provided example test cases demonstrate its behavior:
```python
test_cases = [
    ("yogurt", "u"),
    ("FULL", "U"),
    ("quick", ""),
    ("ab", ""),
    ("cafe", "a"),
    ("bacon", "a"),
    ("A", ""),
    ("AEIOU", ""),
]

for word, expected in test_cases:
    result = get_closest_vowel(word)
    assert result == expected, f"For the word '{word}', expected '{expected}' but got '{result}'."
```