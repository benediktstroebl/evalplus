```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([-5, -3, -10, -100]) == -100
assert not_positive([1, 2, 3])
``` 
This Python script defines a function `max_element` that returns the maximum element from a given list. It also defines a specific function `not_positive` that checks whether a list contains only positive numbers.