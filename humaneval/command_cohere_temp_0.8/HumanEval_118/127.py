```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'AEIOUaeiou'  
    # Ensure casing is considered
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    index = next((i for i, char in enumerate(word, 1) if char in consonants), None)
    while index < len(word):
        char = word[index]
        if char in vowels:
            if index == 0 or word[index-1] in consonants:
                return char.upper() if word[index].isupper() else char
            index += 1
        else:
            index += 1
            if index < len(word) and word[index] in consonants:
                index += 1
            else:
                break
    return ''
```

The script relies on the Python languages' abilities to handle strings and iterate over characters. It uses several regex-like ideas but without actual regex usage. It also takes advantage of Python's case sensitivity for strings.

The `next()` function is used on a generator expression `(i for i, char in enumerate(word, 1) if char in consonants)` to find the first index of a consonant. It will loop over the characters in `word` from index 1 (skipping the first, assuming that the starting vowels don't count), checking each character with the condition `char in consonants`. The `enumerate()` is used to get the index of the character. The `next()` will return the first consonant index or `None` if no consonants are found.

Then, it enters a while loop with the condition `index < len(word)` to check the characters after the found consonant, or the whole word if no consonant was found. It assumes that vowels between consonants are the desired ones. 

In the loop:
1. It fetches the character at the current index, `char = word[index]`.
2. It checks if this character is a vowel. If it is, it checks if it's the starting consonant or if the previous character is a consonant. If those are fulfilled, the function returns the character, converted to uppercase if the word is uppercase. 
3. If the character isn't a vowel, it increments the index by 1. Then it checks if the new index is within the word bounds and if the character at this index is a consonant. If those are fulfilled, it increments the index again (to skip the vowel). Otherwise, it breaks the loop. 

The `break` statement will be hit either when a vowel is found between two consonants or when there are no more characters, and the loop will end. 

If no valid vowel is found in the whole word, the loop won't find a consonant after the initial consonant (if there was any), and it will break from the loop. In this scenario, the function will return an empty string `{}`.