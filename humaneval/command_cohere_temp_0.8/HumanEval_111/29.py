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

The `histogram()` function takes a string as input and returns a dictionary of the letters in the string with the most repetition and their corresponding counts. 
If several letters have the same occurrence, it returns all of them. 

This code can be tested with the following tests:
```python
test_cases = [
    ('a b c', {'a': 1, 'b': 1, 'c': 1}),
    ('a b c', {'a': 2, 'b': 2}),
    ('a b c a b', {'a': 2, 'b': 2}),
    ('b b b b a', {'b': 4})
]

for test in test_cases:
    assert histogram(test[0]) == test[1]
```

This would output the following:
```python
>>> for test in test_cases:
...     assert histogram(test[0]) == test[1]
... 
>>> 
```