```python
def histogram(test):
    letters = test.strip().lower().split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function splits the input string into a list of individual letters, then removes any leading or trailing whitespace and converts each letter to lowercase. It then initializes a dictionary, `letter_count`, to store the count of each letter. It iterates through each letter in the list and updates the count in the dictionary. If a letter is encountered for the first time, it's added to the dictionary with a count of 1. If the letter is already in the dictionary, its count is incremented. 

Finally, the function returns the `letter_count` dictionary, which provides a histogram of the letter occurrences in the input string.