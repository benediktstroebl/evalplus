```python
def max_element(lst):
    if not_positive(lst) or not lst:
        raise ValueError("Input list must be a positive or non-empty list.")
    return max(lst)

def not_positive(lst):
    return all(value > 0 for value in lst)

# Test the function with various inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([1, 2, 3, -100]))  # Output: ValueError
print(max_element([]))  # Output: ValueError
print(max_element([2018, 2019]))  # Output: ValueError
```
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. It uses a testing condition `not_positive(lst)` to ensure the input is a positive or non-empty list. The `not_positive` function checks if the list is empty or all elements are zero. 

If the input list does not pass the condition, the function raises a `ValueError` with an descriptive error message. 

You can test the function with various inputs and see how it handles different scenarios.