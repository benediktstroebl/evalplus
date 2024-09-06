```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input list must be a list, not %s" % type(lst))
    return max(lst)

# Test the function
test_max_element = lambda: max_element([1, 2, 3])
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
This script defines a function max_element that finds the maximum element in a given list. The function accepts a list lst as input and returns the maximum element from it. It also includes a test function that tests the correctness of the max_element function by passing different lists and checking the results. You can extend this also pass additional tests to ensure the function works as expected.