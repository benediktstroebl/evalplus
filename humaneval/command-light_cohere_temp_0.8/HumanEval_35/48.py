```python
def max_element(lst):
    if not_element(lst) == None:
        return None
    return max(lst)

def not_element(lst):
    if isinstance(lst, list):
        return max(map(not_element, lst))
    elif isinstance(lst, str):
        return len(lst) > 0
    else:
        raise TypeError("Input must be a list or string")

# Test cases
print("Result of max_element([1, 2, 3]):", max_element([1, 2, 3])) # Output: 3
print("Result of max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])):", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print("Result of max_element('"))", max_element("")) # Output: TypeError: Input must be a list or string
```

This script defines a function max_element that calculates the maximum element in a given list. It also defines a maximum element of a list using the map function and the length of a string as tests for the input.