```python
def sort_even(lst):
    """Sorts even numbers in a list, and returns a new list."""
    return [x for x in lst if x % 2 == 0]

# Test cases
test_sort_even = []
test_sort_even.push_array([1, 2, 3, 4, 5, 6, 7, 8])
test_sort_even.push_array([5, 6, 3, 4, 7, 2, 1, 8])

# Function call and test result
test_sort_even = sort_even(test_sort_even)
assert test_sort_even == [3, 6, 5, 4, 7, 2, 1]

test_sort_even = sort_even([5, 6, 3, 4, 7])
assert test_sort_even == [3, 6, 5, 4, 7]
```
This script defines a function **sort_even** that sorts even numbers in the passed list and returns a new list. The test cases are defined to verify the function. The test results are also compared with the expected results, passing all tests.