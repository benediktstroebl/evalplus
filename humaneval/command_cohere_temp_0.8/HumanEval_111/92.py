```python
def histogram(test):
    letters = test.strip().lower().replace(" ", "")
    if not letters:
        return {}
    frequency = {}
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency
```
The function uses a few string methods to simplify the task. `strip()` removes leading and trailing whitespaces. `lower()` converts the letters to lowercase. `replace(" ", "")` simplifies consecutive spaces into a single one and removes them. Then, it uses a dictionary to count the letter occurrences. If the letter is already in the dictionary, its count is incremented. Otherwise, it's added to the dictionary with a count of 1. This approach handles the scenario of handling multiple letters with the same occurrence.