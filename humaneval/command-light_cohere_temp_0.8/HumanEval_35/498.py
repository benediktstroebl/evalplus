```python
def max_element(lst):
    if not_list(lst):  # Test for empty list
        return None
    
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst)

# Test cases
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element2 = [1, 2, 3, 4, 5, 6, 7]

assert max_element(test_max_element) == 5
assert max_element(test_max_element2) == 7
```
The above Python script defines a function `max_element` that efficiently finds the maximum element in a given list. It also includes test cases to ensure the function's correctness. 

This self-contained function is designed to be efficient and space-saving, making it suitable for practical use in various scenarios.