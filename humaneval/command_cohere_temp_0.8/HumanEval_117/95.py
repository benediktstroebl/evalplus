```python
def count_consonants(word):
    return sum(1 for char in word if char.isalpha())

def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result
```
The `count_consonants` helper function calculates the total count of consonants in a given word. It iterates through each character in the word and checks if the character is an alphabet character, contributing a count of 1 for each consonant. 

The `select_words` function takes the input string `s` and integer `n` as arguments. It splits the input string into a list of words using space as the delimiter. Then, it iterates through each word in the list and checks the count of consonants using the `count_consonants` helper function. If the count is equal to `n`, the word is included in the `result` list. Finally, the function returns the list of words from the input string that contain exactly `n` consonants.

This solution uses only Python's built-in features, and does not rely on any external libraries, ensuring it is self-contained.