```python
def histogram(test):
    letters = test.lower().strip().split()
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
```
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function converts the input test to lowercase, strips any leading or trailing spaces, and then splits it into a list of individual letters. It then initializes a dictionary, `letter_count`, to store each unique letter and its corresponding count. It iterates through each letter in the list of letters, increments its count in the `letter_count` dictionary, and assigns it a count of 1 if it's encountered for the first time. 

The function returns the `letter_count` dictionary, which provides a count of occurrences for each letter in the input `test`.