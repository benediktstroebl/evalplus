```python
def max_element(lst):
    if not_elements(lst):  # Check if list is empty
        return None
    
    max_ = max(lst)  # Initialize max element with the first element of the list
    return max

def not_elements(lst):
    return not lst or len(lst) == 0

# Test cases
print("Max element:", max_element([1, 2, 3]))  # Output: 3
print("List is empty:", not_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: True
```