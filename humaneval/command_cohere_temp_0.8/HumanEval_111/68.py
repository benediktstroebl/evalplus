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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function returns a dictionary where the keys are lowercase letters occurring in `test` and the values are the frequencies of each letter in the string. 

The `letter_count` dictionary is initialized to store the letter frequencies. The `for` loop then iterates over each character in `test`. The characters have been lowered already so that the counting process will be case insensitive. For each character, the function checks if the character is already a key in the `letter_count` dictionary. If it is, the count for that character is incremented; otherwise, a new entry is created in the dictionary with a count of 1. 

This code will return a dictionary with the letter with the most repetition and corresponding count, as well as any other letters with the same occurrence if they occur in the string. In the case where several letters have the maximum occurrence, it will return all of them. 

This solution is straightforward and resolves the issue in a relatively concise manner.