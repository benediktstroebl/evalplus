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
This Python script uses the `histogram()` function to create a dictionary that maps each lowercase letter in a given string to the number of times that letter appears in the string. The script first removes any leading and trailing whitespace and then splits the string into individual letters before checking for letter occurrences in the `letter_count` dictionary. The function then returns the dictionary with the results. 

This approach ensures that the code is efficient and easy to understand, following standard Python best practices.

You can test this function with the following tests and evaluate its behavior:
```python
test_cases = [
    ('a b c', {'a': 1, 'b': 1, 'c': 1}),
    ('a b c a b', {'a': 2, 'b': 2}),
    ('a b c a b', {'a': 2, 'b': 2}),
    ('b b b b a', {'b': 4}),
    ('', {}),
]

for test, expected in test_cases:
    result = histogram(test)
    assert result == expected
```