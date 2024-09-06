```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qwerty':
                cons_count += 1
        else:
            continue
    
    if cons_count > 1:
        if word[-2].lower() in 'aeiou':
            return word[-2]
    elif cons_count == 1:
        if word[-1].lower() in 'aeiou':
            return word[-1]
    return ''
```

This script employs a loop to inspect each character in the `word` parameter. It assesses whether each character is a consonant or vowel, tallying consonsant characters with the `cons_count` variable. The function returns the last vowel character if two consonants are followed by a vowel. If only one consonant is present, the function returns the isolated consonant. If no viable vowels are found, the function returns an empty string. 

The `continue` statement facilitates skipping special characters, solely focusing on alphabetic characters. This enables the function to adeptly address the `word` parameter, returning the optimal result.