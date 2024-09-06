```python
def histogram(test):
    letters = test.strip().lower().split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```

The code works by first stripping and lowercasing the input `test` so that it can handle whitespace and case insensitivity. It then uses `split()` to convert the string into a list of individual letters. A dictionary `letter_count` is used to store the counts of each letter as they are encountered. Finally, the function returns the dictionary containing the letter counts.