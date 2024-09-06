```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
values_test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

for case in values_test_cases:
    actual = filter_integers(case)
    assert len(actual) == len(case)
    assert all(actual == [x for x in case if type(x) == int])
```  The code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input list. It employs a filter expression `[x for x in values if type(x) == int]` to filter out non-integer values from the input list. 

The code then tests the function by creating a list of test cases, which includes both lists of integers and lists of non-integer values. It iterates through list of test cases and calls the `filter_integers` function with each test case. 

It then verifies that the length of the actual output is the same as the expected length and that each element in the actual output matches the corresponding element in the input test case if it is an integer.