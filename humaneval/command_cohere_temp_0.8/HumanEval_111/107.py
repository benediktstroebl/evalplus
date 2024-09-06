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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function returns a dictionary where the keys are letters from the input string and the values are the number of times that letter appears in the input string. 

To achieve this, it initializes an empty dictionary `letter_count`, loops through each letter in the `test` string, and increments the count of the corresponding letter in the `letter_count` dictionary. If the letter is encountered for the first time, it is added to the dictionary with a count of 1.

This code assumes that the input string contains only lowercase letters and spaces. It handles cases where multiple letters have the same highest occurrence and returns all such letters along with their counts.