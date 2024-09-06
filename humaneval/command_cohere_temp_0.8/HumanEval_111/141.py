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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function splits the input string into a list of individual letters using the `split()` method. It then initializes an empty dictionary called `letter_count` to count each letter's occurrence. It iterates through each letter in the list, and if the letter is already a key in the `letter_count` dictionary, its count is incremented. If not, it's added to the dictionary with a count of 1. 

Finally, the function returns the `letter_count` dictionary, which provides the count of each letter in the input string.