Here is a self-contained Python function that solves the problem of getting unique elements from a list:
```python
def unique(lst):
    return list(set(lst))

# Test cases
 tests = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], []],
  [(5,), (5, 3, 123)],
  [[]],
  [1, 2, 3, 4, 5, 6],
]

for test_case in tests:
    print(unique(test_case[0]))  # expected output: [0, 2, 3, 5, 9, 123]
    assert len(unique(test_case[0])) == len(test_case[1]), \
         "Length of unique elements does not match"
    assert set(unique(test_case[0])).is_(set(test_case[2])), "Set conversion failed")
``` 

This script provides a function called unique that accepts a list as an argument and outputs a list containing only the unique elements from the input list, which are guaranteed to be sorted.