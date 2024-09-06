Here's a Python script that contains a function to solve the problem you've described:
```python
def count_consonants(word):
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        ct = count_consonants(word)
        if ct == n:
            result.append(word)
    return result
```

The `count_consonants` helper function calculates the number of consonants in a given word, ensuring a more concise and efficient main function. The `select_words` function splits the input string into words, iterates through each word, and retains those with exactly n consonants.

This solution surpasses the given examples in clarity and efficiency, leaving room for more comprehensive tests. To truly validate the function, testing various input lengths, word patterns, and diverse consonant counts is essential. This will reinforce the function's reliability and adaptability to real-world scenarios.