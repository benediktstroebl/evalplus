```python
def unique(l: list):
    return list(set(l))

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [19, 2, 1, 4]
assert unique(test_case2) == [2, 1, 4]

# Test case 3
test_case3 = ['a', 'apple', 'band', 'bas', 'bc']
assert unique(test_case3) == ['a', 'apple', 'band', 'bas', 'bc']

# Test case 4
test_case4 = {'a': 2, 'b': 3, 'c': ['d', 'e'], 'f': [1, 2, 3]}
assert unique(test_case4) == {'a': 2, 'b': 3, 'c': ['d', 'e'], 'f': [1, 2, 3]}
```
This script defines a function unique that takes a list as input and returns a new list with unique elements from the original list, using the set() function to get the unique elements. The test suite includes several test cases to verify the correctness of the unique function. The output of each test cases should match the expected results.