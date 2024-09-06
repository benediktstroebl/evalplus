```python
def unique(lst):
    return sorted(set(lst))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'b', 'c', 'd'],
    [1, 2, 4, 6, 7, 8, 9]
]

for item in test_unique:
    assert unique(item) == set(item)
```  This Python code defines a function called unique that returns a set of unique elements from a given list. The function employs the unique elements in the list using the `set()` function and the `sorted()` function with `set(set())` to identify and return unique values. The code includes a test cases to validate the correctness of the `unique()` function, and uses a `for` loop to iterate over each test case and asserts that the output of the `unique()` function matches the expected set of unique elements.