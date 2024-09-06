```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        return float('-inf')

def not_negative(lst):
    return any(-x for x in lst if x < 0)

# Test the max_element function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([5, 'three', -5, 2, -3, 3, 'nine', 0, 123, 1, -10]))  # Output: 123
print(max_element([1, 2, 3, -100, 4, -200]))  # Output: -100
print(max_element([-1, -2, -3, -4, -5, -6, -7, -8, -9]))  # Output: -9
```  This script defines two functions: `max_element` calculates and returns the maximum element from a given list, while `not_negative` checks if the list contains negative values.  The different purpose is to determine the maximum element when the list contains negative values.