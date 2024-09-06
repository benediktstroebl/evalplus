```python
def histogram(test):
    letters = test.split()
    histogram = {}
    for letter in letters:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram
```
The `histogram` function first splits the test string into a list of letters. Then, it iterates through this list, updating the count of each letter in the `histogram` dictionary. If a letter is encountered for the first time, it is added to the dictionary with a count of 1. If it is already present, its count is incremented. 

This approach guarantees the correctness of the problem in all the mentioned test cases.