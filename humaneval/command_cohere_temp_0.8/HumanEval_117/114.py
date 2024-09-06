```python
def count_consonants(word):
    counts = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                counts += 1
    return counts

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The provided Python script implements a function called `select_words(s, n)` that takes a string `s` and an integer `n` as input. This function returns a list of all words from the string `s` that contain exactly `n` consonants. It assumes the input string contains only letters and spaces.

The script also defines a helper function, `count_consonants(word)`, which calculates the number of consonants in a given word. This function counts the number of letters that are not vowels (assuming the lowercase letters 'a', 'e', 'i', 'o', and 'u' are vowels).

The `select_words` function first splits the input string `s` into a list of words using spaces as separators. Then, it iterates through each word in the list and calculates the number of consonants using the `count_consonants` function. If the consonant count matches the required count `n`, the word is added to the `result` list. Finally, the function returns the list of selected words.

This code solves the problem by identifying words in the input string that have the specified number of consonants and retrieves them as a list, accordingly.