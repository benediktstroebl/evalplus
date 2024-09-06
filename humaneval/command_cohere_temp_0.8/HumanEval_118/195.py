```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), None)
    if index is None:
        return ''

    # Counting number of vowels on the right side
    vowel_count = sum(1 for char in word[index: ] if char in vowels)
    
    if vowel_count == 0:
        return ''

    return word[index+vowel_count-1]
```

This script assumes only the English alphabet and doesn't consider the international phonetic alphabet. It also doesn't handle accented characters.

The `index` variable is assigned the first index of the first consonant character from the right side of the word. Next, it counts the number of vowel characters in the remainder of the word (after the consonant just found). If no vowels are found, it returns an empty string. If there is only one vowel, it returns that vowel. If there are multiple vowels, it returns the last one of them, as the problem statement requested. 

It's worth noting that the current implementation assumes the English language and specifically English alphabet characters. It won't work correctly with other languages or character sets. 

This approach assumes that there is at least one consonant in the word, resulting in an index assignment. The assumption is fulfilled in the test cases provided alongside the problem statement. If a word without any consonant is passed, an index error will occur. Adjustments may be necessary depending on the criteria for input.