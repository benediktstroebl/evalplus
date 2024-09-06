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

The `letter_count` dictionary is initialized to store the letter counts. The `for` loop then iterates over each letter in the `test` string. The letters are transformed to lowercase to ensure that the counting process ignores the case and counts letters accordingly. The frequency of each letter is then updated by incrementing the count if the letter is already in the `letter_count` dictionary, or by adding the letter with a count of 1 if it's not already in the dictionary. 

This solution is efficient and has a time complexity of O(n), where n is the length of the input string `test`.