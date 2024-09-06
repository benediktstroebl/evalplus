```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test cases
test_cases = [
    [ [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123] ],
    [[]],
    [ [10, 20, 30], []],
    [ [100, 200, 300], [200, 300, 100, 200, 300]]
]

for i, test_t in enumerate(test_cases):
    actual = incr_list(test_t)
    expected = list(map(lambda x: x+1, test_t))
    assert actual == expected, f"Test {i+1} failed: {actual} != {expected}"
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function uses list comprehension and the same list l to achieve this. 

The code then provides test cases for the incr_list function, creating a list of test cases.

The test_cases list contains four test cases, each containing a list of values to be tested. The test_cases list is then looped over using the enumerate function, and the incr_list function is called with each test case. The resulting list of values is compared with the expected list of values using the assert function, with an error message displayed if the two lists do not match.