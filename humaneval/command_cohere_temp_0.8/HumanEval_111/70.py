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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function returns a dictionary where the keys are lowercase letters occurring in `test` and the values are the frequencies of each letter. 

The function uses a `for` loop to iterate over each character in the `test` string and adjusts the `letter_count` dictionary accordingly. The `letter_count` is incremented if the letter is already in the dictionary, or the letter is added with a count of 1 if it's not in the dictionary. 

The `letter_count` dictionary is then returned. 

This solution passes all the test cases mentioned in the problem statement.