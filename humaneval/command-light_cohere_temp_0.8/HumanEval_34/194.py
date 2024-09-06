```python
def unique(lst):
    return list(set(lst))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [0, 2, 3, 5, 9, 'abc', '123'],
]

for item in test_unique:
    actual = unique(item)
    assert actual == [0, 2, 3, 5, 9, 'abc', 123]
```

This code defines a function unique that returns a list of unique elements from an input list lst by using the set() function. It also provides a test cases to test the function, passing in a list of numbers and a string, and checking that the output list contains the expected elements. The test cases will also validate that the function returns the correct unique elements.