```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test the function with various inputs
tests = [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123],),
    ([-5, -2, 0, 'abc', 123],),
    ([121, 12, 2345, 0, 0, 1],),
    ([2, 2, 2.doc2, true, list([0, 2, 3, 5, 9, 123])],),
    ([0, 2, 3, 5, 9, 123, [123, 124], [123, 124]]),
    ([-, []],),
    ([10, ]),
]

for test_case in tests:
    print("Test:", test_case)
    assert unique(test_case) == [0, 2, 3, 5, 9, 123]
 ``` 
This script defines a function called unique, which takes a list as input and returns a new list containing only the unique elements from the input list. The function uses a set to keep track of the unique elements. The test suite contains various test cases, which cover a variety of input scenarios, and the function is tested with each case to ensure its correctness.