```python
def max_element(lst):
    if not_positive(lst):  # Initialize the maximum as the smallest positive number
        max_element = min_positive(lst)
    else:
        max_element = lst[0]
    for num in lst:  # Compare each element to the current maximum and update if greater
        if num > max_element:
            max_element = num
    return max_element

def not_positive(lst):
    return all(num > 0 for num in lst)

def min_positive(lst):
    return lst[0] if not_positive(lst) else min(lst)

# Test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert not_positive([100, 200, -500]) and max_element(not_positive([100, 200, -500])) == -500
assert not_positive([4, -4]) and max_element(not_positive([4, -4])) == 4
```

This Python code defines a function `max_element` that finds the maximum element in a list, and a related function `not_positive` to test if the input list contains only positive numbers, in which case the function returns the smallest positive number. The function also includes a `min_positive` function to find the minimum positive number in a list. This ensures that the correct result is returned for cases with negative numbers as well.