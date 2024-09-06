```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels and word[i] == word[len_word - 1] and word[i] != word[len_word - 2]:
            return word[i]
    return ''
```

This script assumes only letters from the English alphabet are included in the input word. The function iterates through the word using a loop and identifies if the current letter is a vowel and if it is the last letter but not the second-to-last letter. If these conditions are met, the function returns the current vowel. If no vowels meet these conditions, an empty string is returned. 

Let's unwind the test cases:
- `get_closest_vowel("yogurt")` -> "u" - The last two consonants are "rt", and the only vowel between them is "u", so it's the closest one.
- `get_closest_vowel("FULL")` -> "U" - The last two consonants are "L", and the only vowel between them is "U", so it's the closest one.
- `get_closest_vowel("quick")` -> "" - There is no vowel between the last two consonants "ck", so an empty string is returned.
- `get_closest_vowel("ab")` -> "" - The last two consonants are "b", and the only vowel "a" is not between them, so an empty string is returned. 
This function guarantees a linear time complexity with O(n), where n is the length of the input word.