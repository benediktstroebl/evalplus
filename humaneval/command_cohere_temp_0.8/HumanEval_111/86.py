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
This Python script defines a function called `histogram` which takes in a single argument, `test`. The function returns a dictionary where the keys are the most frequent letters in `test` and the values are the corresponding counts. 

To accomplish this, it initializes an empty dictionary called `letter_count`. It then iterates through each letter in the `test` string, converting each letter to lowercase. If the current letter is already in the `letter_count` dictionary, it increments its count. If not, it adds the letter to the dictionary with a count of 1. 

The function returns the `letter_count` dictionary after processing all letters in `test`. 

This approach ensures that the function handles multiple letters with the same highest occurrence, as specified in the exercise details.