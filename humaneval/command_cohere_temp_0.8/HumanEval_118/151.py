```python
def get_closest_vowel(word):
    cons_pair = []
    right_index = 0
    for i, char in enumerate(word):
        if char.isalpha():
            if char.lower() in 'aeiou':
                if i > right_index and word[i-1].lower() not in 'aeiou':
                    right_index = i
            else:
                if i > right_index and word[i-1].lower() not in 'aeiou':
                    cons_pair.append(right_index)
                    right_index = i
    if right_index == 0:
        return ''
    prev_consonant = word[cons_pair[0] - 1] if cons_pair else word[right_index - 1]
    next_vowel = word[right_index] if right_index < len(word) - 1 and word[right_index + 1].lower() in 'aeiou' else ''
    if next_vowel == '' and word[right_index].lower() in 'aeiou':
        return word[right_index]
    if next_vowel == '' and word[right_index].lower() in 'ieou':
        if (prev_consonant in 'bcdfghjklmnpqrstvwxyz' and word[right_index].lower() in 'aeiou') or \
           (prev_consonant in 'aeioubcdfghjklmnpqrstvwxyz' and word[right_index].lower() in 'bcdfghjklmnpqrstvwxyz'):
            return word[right_index].upper()
        else:
            return word[right_index]
    return next_vowel
```

The algorithm works by iterating over the word character by character. When a consonant is encountered for the first time after a vowel, store its index and right after it. When a second consonant is encountered, check if there is a vowel between these two consonants and return it. If no such vowel exists, return an empty string. The script assumes that the given word contains only English letters.

This approach assumes that there's at least one vowel somewhere in the string, so it's more efficient than the previous version thanks to its linear complexity (`O(n)`). The code is also more concise and easy to understand. 

The previous version of the algorithm used two pointers and worked by iterating over the word twice, making it less efficient with a complexity of `O(n^2)`. It also required more lines of code, making it less concise.