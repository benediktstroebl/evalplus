```python
def max_element(lst):
    return lst[-1] if len(lst) == 1 else lst[-1] + max(lst[:-] or lst[-2:])

# Test cases for the function
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == 123
assert(max_element([1, 2, 3]) == 3)
assert(max_element([-5, -3, -10]) == -10)
assert(max_element([]) == 0)
assert(max_element([42, -100])) == None
```