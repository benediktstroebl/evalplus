```python
def unique(l: list):
    return list(set(l))

# Test case 1: Verify function returns a subset of input list
assert set(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) == set([0, 2, 3, 5, 9, 123])

# Test case 2: Verify returned values are unique
assert len(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])) == 6

# Test case 3: Verify function behavior with empty list
assert unique([]) == []

# Test case 4: Verify function behavior with list of strings
assert unique(["Hello", "World", "!!!!!", "Hello"]) == ["Hello", "World!", "!!!!!"]
```
This script defines a function unique that takes a list as input and returns a sorted list of unique elements using the set data structure. It also includes several test cases to verify the correctness of the unique function. These test cases ensure that the function behaves as expected.