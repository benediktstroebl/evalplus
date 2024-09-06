```python
def max_element(lst):
    return lst[-1] if lst and lst[-1] > all(lst[:-]) else lst[-1]

# Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert not max_element([])
assert not max_element([5, 0, -5])
```