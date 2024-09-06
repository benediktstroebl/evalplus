```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test cases
test_incr_list = [
    [
        (=[1, 2, 3], [1]),
        ( [5, 3, 5, 2, 3, 3, 9, 0, 123], [5, 3, 5, 2, 3, 3, 9 ]),
        ( [(), [], True], [1, 2, 3])
    ]
]

def test_func(test_case):
    """Test the incr_list function with the given test case."""
    assert list(incr_list(test_case)) == test_case[1]

for test in test_incr_list:
    test_func(test)
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements from input list incremented by 1. 

The code also includes a set of test cases, each containing a list to be passed to the incr_list function for testing. 

Finally, the test_func function tests the incr_list function with each test case, ensuring the expected results are achieved.