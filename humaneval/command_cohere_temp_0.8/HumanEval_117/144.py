```python
def count_consonants(word):
    consonants = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
    return consonants

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first defining a function `count_consonants` that calculates the number of consonants in a given word. It then defines the main function `select_words` which splits the input string into a list of words, and then iterates through the words to select the words that have exactly the desired number of consonants. The selected words are added to the `result` list and returned.

This solution aims to fulfill the requirement of returning the list of words containing exactly 'n' consonants, in the order they appear in the string 's'.