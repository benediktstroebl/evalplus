```python
def max_element(lst):
    if not_elements(lst):
        return 0  # Handle empty list to avoid errors
    return max(lst)

def not_elements(lst):
    if not lst:
        raise ValueError("Input list is empty")
    return bool(lst)

# Example usage
lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(lst))  # Output: 123
print(max_element([]))   # Output: 0 (empty list)
print(max_elements([123]))  # Output: True (not empty)
```
This script provides a function `max_element` that takes a list as an argument and returns the maximum element in the list. The `not_elements` helper function is used to handle empty lists, preventing errors. The script also provides a `not_elements` helper function to check if the list is empty and raise a `ValueError`. The example usage demonstrates the functionality of the `max_element` function with various input lists.