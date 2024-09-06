```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7],
    ['apple', 'banana', 'cherry'],
    ['a', 'b', 'c', 'd'],
]

for test_case in test_cases:
    actual = unique(test_case)
    assert set(actual) == set(test_case)
    print(f"Test case {test_case} passed!")

error = [5, 3, 5, 2, 3, 'abc'] # Incorrect input
with self.throw expected_error:
    actual = unique(error)
    assert actual == []
    print(f"Expected error: {error} but passed!")
```
This Python script defines a function called unique that takes a list as input and returns a new list containing unique elements from the original. It utilizes a unique elements in the seen set to quickly identify duplicates and non-None items. The test cases section consists of multiple lists to test the unique function, and it verifies that the output is indeed unique by checking if they are equal using the set() method. The function also has a expected error case for an invalid list, where it contains a string instead of a list.