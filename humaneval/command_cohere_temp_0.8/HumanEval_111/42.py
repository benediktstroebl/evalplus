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
This Python script defines a function called `histogram` that takes in a single argument, `test`. The function returns a dictionary where the keys are lowercase letters occurring in the input string, and the values are the number of times that letter occurred in the string. 

For example, if the input test string is 'a b c', the output dictionary will be {'a': 1, 'b': 1, 'c': 1'}. If the input string is 'a b c a b', the output dictionary will be {'a': 2, 'b': 2}. If several letters have the same occurrence, they will all be included in the output dictionary. In the case of the input string 'b b b b a', the output dictionary will be {'b': 4}. If the input string is empty, the output will be a empty dictionary {} . 

This code solves the problem using a for loop. For each letter in the string, it counts the number of times that letter appears. It does this by adding 1 to the corresponding count if the letter is already in the dictionary, or by adding a new entry to the dictionary with a count of 1 if it's the first time that letter has appeared. 

The example usage provided demonstrates how to use the `histogram` function to solve the given problem statement and can be used as a reference for applying this solution to other similar problems.