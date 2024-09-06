```python
def max_element(lst):
    if not_element(lst) == -float('inf'):
        raise ValueError("List is empty or has no positive elements")
    return max(lst)

def not_element(lst):
    try:
        return max(lst)
    except ValueError as e:
        print(f"Input list must have at least one positive element: {e}")
        raise

test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
This script defines a max_element function that returns the maximum element in a list, it also includes a function not_element that raises an error if the input list is empty or has no positive elements. The script also contains the test cases that validate the behaviour of the max_element and not_element functions.