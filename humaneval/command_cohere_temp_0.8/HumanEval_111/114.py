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
The function creates a dictionary called `letter_count`, where the keys are letters and the values are their occurrences in the given test string. Using a for loop, it iterates through each letter in the test string and checks if the letter is already a key in the `letter_count` dictionary. If it is, the corresponding value is incremented by 1, otherwise, it is added to the dictionary with a value of 1. Ultimately, the function returns the `letter_count` dictionary.

This solution should be able to handle cases with letters that have multiple occurrences and return the correct dictionary in the event of a tie.