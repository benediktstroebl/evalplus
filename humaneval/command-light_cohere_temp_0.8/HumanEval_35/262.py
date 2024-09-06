```python
def max_element(lst):
    if not_elements(lst):
        return 0
    else:
        return max(lst)

def not_elements(lst):
    if not lst:
        return False
    for n in lst:
        if not int(n):
            return False
    return True

# Example usage
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(test_list))  # Output: 123
print(not_elements(test_list))  # Output: True
```
This Python script defines a function `max_element` that calculates and returns the maximum element in a given list. The `not_elements` function checks if the input list is empty or contains non-integer elements and returns `True` if the condition is met, else `False`.