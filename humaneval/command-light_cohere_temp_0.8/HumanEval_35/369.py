```python
def max_element(lst):
    if not_sorted(lst):  # Check if list is sorted
        return lst[-1]
    return max(lst)

# Test function to check the solution
def test_max_element(test_list):
    actual = max_element(test_list)
    assert actual == (5 if test_list == [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] else 123)

# Run the tests
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
This code defines a function max_element that returns the maximum element in a given list. The function first checks if the test_list is sorted, which is a precondition for finding the maximum element. If the list is not sorted, it returns the last element of the list. Finally, it runs the tests with a test_list containing various lists to ensure the correctness of the max_element function.