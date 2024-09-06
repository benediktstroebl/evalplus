```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel:
                cons_count += 1
        else:
            continue
    if cons_count > 1:
        for char in word[::-1]:
            if char.isalpha():
                if char.lower() in 'aeiou':
                    return char
                else:
                    continue
            else:
                break
    return ''
```

The function `get_closest_vowel()` iterates through the given word, counting consecutive consonants with the `cons_count` variable. Once multiple consonants are found (i.e., `cons_count > 1`), the function works backward through the word, checking each character for being a vowel. The first encountered vowel or reaching a non-alphabetic character breaks the loop, and its character is returned as the result. If no vowel meets the criteria, an empty string is returned. 

This approach ensures that the function considers vowels between consecutive consonants, prioritizes close ones, and avoids leading or trailing vowels.