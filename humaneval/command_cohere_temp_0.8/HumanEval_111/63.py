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
The `histogram()` function takes a single string `test` as input, which represents a space-separated sequence of lowercase letters. It splits the input into a list of individual letters and then iterates through them to populate a dictionary called `letter_count`. This dictionary stores each letter as a key and its corresponding occurrence count as the corresponding value. If a letter is encountered that is already in the dictionary, its count is incremented; otherwise, a new entry is created with a count of 1. 

The function returns this dictionary `letter_count`, which provides a histogram of the letter occurrences in the input string. If multiple letters have the same occurrence count, they will all be included in the result. The example provided in the prompt would result in the following output:
```python
histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
```

This approach is concise and efficient, providing a clear and functional solution to the problem.