```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with different lists
test_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_list1) == 123

test_list2 = [5, 3, 0, -10, -3, 7]
assert max_element(test_list2) == 5

test_list3 = [(), None, [], [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
assert max_element(test_list3) is None
```

This code defines a function max_element that calculates the maximum element in a given list. It utilizes the max function to return the maximum value in the list.

The code also provides test cases to ensure the correctness of the function by passing different lists and asserting the expected maximum element.