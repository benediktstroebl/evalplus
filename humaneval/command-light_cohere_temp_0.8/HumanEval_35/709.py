```python
def max_element(lst):
    return lst[-1] if len(lst)>0 else None

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([]) is None

# Test case 4
try:
    l = ['a', 'bb', 'ccc']
    x = max_element(l)
    assert x == 'bb'
except Exception as e:
    print("Error:",e)
```