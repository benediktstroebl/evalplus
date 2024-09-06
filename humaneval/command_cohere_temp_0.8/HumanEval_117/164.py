```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                cnt += 1
    return cnt

def select_words(s, n):
    words = []
    word = ""
    for c in s:
        if c == ' ':
            if count_consonants(word) == n:
                words.append(word)
            word = ""
        else:
            word += c
    if count_consonants(word) == n:
        words.append(word)
    return words
```
The provided Python script implements a function called `select_words(s, n)` that takes a string `s` and an integer `n` as input. This function returns a list of all words from the string `s` that contain exactly `n` consonants. It iterates through the characters of the input string `s`, identifying word boundaries whenever it encounters a space character. For each word, it calculates the number of consonants using a predefined function `count_consonants(word)`, which counts the number of consonants (including capitalized consonants) in the word. If the word contains exactly `n` consonants, it's added to the `words` list. After processing the entire string, the function returns a list containing all the words that meet the criterion for having exactly `n` consonants. This solution ensures that the list of returned words is ordered correctly, as it respects the order of words in the original string.