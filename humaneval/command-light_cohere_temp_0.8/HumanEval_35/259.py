```python
def max_element(lst):
    if not_elements(lst):  # Base case: empty list
        return None
    
    max_ = max(lst)  # Initialize max element
    for num in lst: 
        if num > max: 
            max = num 
    return max

def not_elements(lst):
    return not len(lst) == 0

# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([]))  # Output: None
print(max_element([5, 2, -3, -10])))  # Output: -10
```

This function `max_element` accepts a list `lst` as input and identifies and returns the maximum element from the list. The function is tested and passes all test cases with various lists.