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
The function creates a dictionary, letter_count, that stores the count of each letter encountered in the input string. The `lower()` method is used to ensure that the letters are compared case insensitively. It iterates over each letter in the test string, if the letter is already in the letter_count dictionary, the count is incremented; otherwise, it's added to the dictionary with a count of 1. This way, the function properly handles the case where several letters have the same occurrence and returns all of them.