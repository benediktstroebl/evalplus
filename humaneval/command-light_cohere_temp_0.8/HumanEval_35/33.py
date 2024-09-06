```python
def max_element(lst):
    if not_element(lst):
        return float('-inf')
    return max(lst, key=lambda x: x)

def not_element(lst):
    try:
        return len(lst) == 0
    except TypeError:
        return False

# Example usage
test_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
# Output: 123
test_not_element([])
# Output: False
``` 
This Python script defines a function `max_element` that finds the maximum element in a given list. It also includes a function `not_element` to check if the list is empty and raises a `TypeError`. The `max_element` function uses the `max` function with a key function to find the maximum element.