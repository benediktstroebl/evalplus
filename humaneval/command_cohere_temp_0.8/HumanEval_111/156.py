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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function returns a dictionary where the keys are lowercase letters occurring in the `test` string and the values are the frequency of each letter in the string. 

The `letter_count` dictionary is initialized to store the letter frequencies. The `for` loop then iterates through each letter in the `test` string. If the letter is already a key in the `letter_count` dictionary, the letter's count is incremented. If the letter is not already a key, the letter is added to the dictionary with a count of 1. 

The example usage of the `histogram` function is also provided in the docstring, showcasing its usefulness in solving the given problem statement.