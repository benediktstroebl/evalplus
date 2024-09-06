```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
                if vowel:
                    cons_count += 1
        else:
            vowel = False

    if cons_count > 1:
        if vowel:
            return char.upper()
        else:
            return ''
    else:
        return ''
```

The Python script provides a function called `get_closest_vowel` which takes in a word as input. This function identifies vowels and counts the number of consecutive consonants in the word. If there are more than 1 consecutive consonants, it returns the closest vowel if one exists, or an empty string if none is found. If there are no consecutive consonants or fewer than 2, the function returns an empty string. 

The script takes into consideration only alphabetic characters and disregards special characters or numbers. Additionally, the script is case-sensitive, so it considers both uppercase and lowercase vowel variations.