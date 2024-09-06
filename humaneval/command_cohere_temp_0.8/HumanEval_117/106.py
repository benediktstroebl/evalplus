```python
def count_consonants(word):
    cs = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cs += 1
    return cs

def select_words(s, n):
    words = []
    s += ' '
    for word in s.split():
        if count_consonants(word) == n:
            words.append(word)
    return words
```
The provided Python script implements a function called `select_words(s, n)` that addresses the problem statement. It returns a list of all words from the input string `s` that contain exactly `n` consonants, in the order these words appear in the string. 

The script also includes a helper function, `count_consonants(word)`, which calculates the number of consonants in a given word. This function iterates through each character in the word and counts the characters that represent consonants.

These consonants are defined as characters belonging to the sets: `['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']` and `['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']`.

The `select_words` function commences by appending a space to the input string `s` to ensure that all words in the string are correctly identified. It then splits the string into individual words using the space character. 

For each word, it checks if the count of consonants in that word matches the required count `n`. If the condition is met, the word is added to the `words` list. Finally, the function returns this list of selected words.

Note: The code assumes that the input string contains only letters and spaces. It effectively handles situations where the string is empty or the requested number of consonants is not achievable.