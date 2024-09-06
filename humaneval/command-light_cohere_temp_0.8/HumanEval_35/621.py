```python
def max_element(lst):
    return lst[-1] if lst and lst[-1] > all(lst[:-]) else lst[-1]

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
try:
    assert max_element([1, 2, 3]) == 3
except AssertionError as e:
    print("Error:", e)

# Test case 3
try:
    assert max_element([-5, -3, -10, -20]) == -20
except AssertionError as e:
    print("Error:", e)
```