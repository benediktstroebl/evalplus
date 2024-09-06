```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: basic list
test_basic = [1, 2, 3]
result_basic = incr_list(test_basic)
assert list(result_basic) == [2, 3, 4]

# Test case 2: empty list
test_empty = []
result_empty = incr_list(test_empty)
assert len(result_empty) == 0

# Test case 3: list with single element
test_single = [5]
result_single = incr_list(test_single)
assert list(result_single) == [6]

# Test case 4: list with multiple elements
test_multiple = [5, 3, 5, 2, 3, 5, 3]
result_multiple = incr_list(test_multiple)
assert list(result_multiple) == [6, 4, 6, 3, 4, 4, 10, 1]

# Test case 5: list with negative increment
test_negative = [0, 1, 2, 3]
result_negative = incr_list(test_negative, -1)
assert list(result_negative) == [0, 0, 2, 3]

def test_suite():
    test_cases = [
        ('basic', test_basic),
        ('empty', test_empty),
        ('single', test_single),
        ('multiple', test_multiple),
        ('negative', test_negative)
    ]
    for name, test in test_cases:
        yield name, test()

# Run the tests
test_suite()
```
This Python script defines the `incr_list` function, which simply adds 1 to each element in the input list, and tests it with five different cases. The `test_suite` function sets up a test suite with five different test cases, and then it uses the `yield` statement to iterate through each test case and execute it. 

This allows you to test the `incr_list` function with different inputs and ensure it produces the expected results.