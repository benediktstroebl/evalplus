```python
def histogram(test):
    letters = test.split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
This Python script defines a function called `histogram` that takes in a string as input. Inside the function, the input string is split into a list of individual letters using the `split()` method. Then, a dictionary called `letter_count` is initialized to keep track of the count of each letter. The loop iterates through each letter in the list, and if the letter is already in the `letter_count` dictionary, its count is incremented, otherwise, it's added to the dictionary with a count of 1. After the loop, the function returns the `letter_count` dictionary containing the results.