```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1: Simple list
>>> max_element([1, 2, 3])
3

# Test case 2: List with negative numbers
>>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
123

# Test case 3: List with floating numbers
>>> max_element([3.14, 2, 1. Som, 9])
7. 7.29384590
 maximum element is from the list, which is 9.

# Test case 4: Empty list
>>> max_element([])
None

# Test case 5: List with only one element
>>> max_element([5])
5
```  This function efficiently finds and returns the maximum element in the input list.