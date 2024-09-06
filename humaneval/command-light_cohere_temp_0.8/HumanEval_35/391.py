```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Unit tests
test_max_element = [
    assert max_element([1, 2, 3]) == 3, "Returned value is not the maximum"
    assert max_element([5, 3, -5]) == 3, "Returned value is not the maximum"
    assert max_element([-5, -3, -10]) == -5, "Returned value is not the minimum"
    assert max_element([-3, 0, 123]) == 123, "Returned value is not the maximum"
]
```
The function max_element in the code takes a list lst as input and returns the maximum element in the list using the max() function. It also includes unit tests with assert statements to check the correctness of the max_element function for different input lists.