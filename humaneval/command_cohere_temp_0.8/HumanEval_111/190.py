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
This Python script defines a function called `histogram` which takes in a single argument, `test`. The function returns a dictionary where the keys are letters from the string `test` and the values are the number of times that letter appears in `test`. 

The `letter_count` dictionary is initialized to store the letters and their corresponding counts. The `for` loop iterates over each letter in the `test` string and checks if the letter is present as a key in the `letter_count` dictionary. If it is, the count for that letter is incremented; otherwise, a new entry for the letter is added with a count of 1. 

The example usage in the Problem Description section demonstrates how the function works for different inputs.