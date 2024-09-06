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

    if cons_count < 2:
        return word[0].lower()

    right_index = len(word) - 1
    vowel_found = False
    for i in range(right_index):
        if word[i].lower() in 'aeiou':
            vowel_found = True
            break

    if not vowel_found:
        return ''

    return word[i].lower()
```

The script counts consonants as we iterate over the letter of the word. It then checks if there are less than two consonants on the right side of the word. If so, it returns the first vowel of the word. If not, it continues iterating over the right side of the word to find the closest vowel to two consonants. If the script couldn't find a vowel between two consonants, it returns an empty string. 

Note that the script assumes that the given word is only English letters, and the script also assumes the word to be case-sensitive, as stated in the prompt.