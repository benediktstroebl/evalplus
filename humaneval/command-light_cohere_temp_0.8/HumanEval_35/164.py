```python
def max_element(lst):
    if not_positive(lst):  # Check if list is empty or all elements are positive
        return float('-inf')  # Return negative infinity
    elif len(lst) == 1:
        return lst[0]
    else:
        max_element = lst[0]
        for num in lst[1:]:
            if num > max_element:
                max_element = num
        return max_element

def not_positive(lst):
    return all(num > 0 for num in lst)

# Unit tests
test_max_element = [
    assert max_element([1, 2, 3]) == 3, "Return 3 for positive list"
    assert max_element([5, 3, -5]) == 3, "Return 3 for positive list"
    assert max_element([9, 0, 123]) == 123, "Return 123 for positive list"
    assert max_element([-5, 3, -3]) == -5, "Return -5 for negative list"
    assert max_element([1, 2, -3, 3]) == 3, "Return 3 for positive list"
]
```

This script defines a function `max_element` that finds the maximum element in a list. The `not_positive` function is used to handle special cases, including empty lists and all positive numbers. The script also includes unit tests to validate the correctness of the `max_element` function.