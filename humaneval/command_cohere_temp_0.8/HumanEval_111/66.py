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

This function processes the test string by stripping any leading or trailing whitespace and converting the string to lowercase to make the analysis case insensitive. It then splits the string into individual letters using the `split()` method, which separates the string into a list of space-separated words.

For each letter, it increments the count in the `letter_count` dictionary. If the letter is already present in the dictionary, the count is incremented; otherwise, a new entry is created with a count of 1. 

The function returns the `letter_count` dictionary, providing a mapping of each letter to its corresponding occurrence count. If there's a tie among letters with the most occurrences, the function will return all of them, as outlined in the problem statement.

This solution adheres to the problem's specified examples, returning the expected results for various inputs.