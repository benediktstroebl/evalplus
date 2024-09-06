```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Finding possible vowels
    possible_vowels = []
    i = len(word) - 2
    while i >= 0 and word[i] not in consonants:
        if word[i] in vowels:
            possible_vowels.append(word[i])
        i -= 1
    # Checking if the possible vowels are between two consonants
    if len(possible_vowels) == 0:
        return ''
    for vowel in possible_vowels:
        if (word[i] in consonants and word[i + 1] in consonants and
                vowel in vowels):
            return vowel
    return ''
```

This Python script defines a function `get_closest_vowel` that aims to find the closest vowel to a specified word's end, assuming that the given word contains only English letters. Here's how it works:
1. First, the English consonants and vowels are stored in two separate strings, `consonants` and `vowels`, for convenient reference.
2. The function initializes an empty list called `possible_vowels`, which will store possible vowels that meet the criteria, and assigns the index `i` to be one less than the length of the input word (`i = len(word) - 2`).
3. A while loop begins, and it will continue as long as `i` is a valid index and the character at index `i` is not a consonant. This loop identifies possible vowels for consideration.
4. If the character at index `i` is a vowel, it's added to the `possible_vowels` list.
5. The index `i` is decremented, moving toward the beginning of the word, and the loop continues to find possible vowels.
6. Once the possible vowels are identified, the function checks if any of them satisfy the problem's conditions. It first checks if no possible vowels were found (`if len(possible_vowels) == 0`), returning an empty string if so.
7. If there are possible vowels, the function loops through each of them to check if they meet the condition of being between two consonants. If it finds a vowel that satisfies this condition, it returns that vowel.

Overall, this well-structured code efficiently identifies the closest vowel to the right end of the word, ensuring it sits between two consonants, and returns an empty string if no such vowel is found.