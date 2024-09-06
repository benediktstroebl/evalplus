```python
def max_element(lst):
    if not_positive(lst) or not_unique(lst):
        raise ValueError("Input list must be either all positive or unique")
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

def not_unique(lst):
    return set(lst) == {list(lst)}

print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
The code defines a function `max_element` that finds the maximum element in a list. Using a helper functions `not_positive` and `unique`, the function ensures the input list is valid, then returns the maximum value. This ensures the code is self-contained and solves the problem of finding the maximum element in a markdown code block.