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
The function creates a dictionary called `letter_count`. It iterates through the input `test` and for each character, it increments the count in the `letter_count` dictionary. If the character doesn't exist in the dictionary, it's added with a count of 1.

The example usage and tests passed. Let me know if you would like assistance with anything else!