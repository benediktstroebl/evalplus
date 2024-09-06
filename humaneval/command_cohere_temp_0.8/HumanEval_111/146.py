```python
def histogram(test):
    letter_count = {}
    for letter in test.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
The function creates a dictionary called `letter_count`. It iterates through each letter in the `test` string, converting each letter to lowercase to ensure the counting process captures all occurrences regardless of case. For each letter, it increments its count in the `letter_count` dictionary. If the letter is encountered for the first time, it is automatically added to the dictionary with a count of 1. This process ensures that the dictionary contains all letters from the input with their respective counts.