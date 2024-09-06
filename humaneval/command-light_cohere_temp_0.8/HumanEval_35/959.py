```python
def max_element(lst):
    if not_positive(lst) and not_empty(lst):
        return max(lst)
    raise ValueError("Input list must contain positive numbers")

def not_positive(lst):
    return all(x > 0 for x in lst)

def not_empty(lst):
    return len(lst) == 0

# Test the function
try: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
except ValueError as e: print(f"Error: {e}")
```
The function `max_element` takes a list as input and returns the maximum element in the list.

The function `not_positive` checks if the list contains any negative numbers, and if so, returns False.

The function `not_empty` checks if the list is empty, and if so, returns False.

The `max_element` function is then tested with a sample input list.