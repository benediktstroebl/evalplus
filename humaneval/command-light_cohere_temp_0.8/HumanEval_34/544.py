```python
def unique(l: list):
    return list(set(l))

# Test case 1
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
[0, 2, 3, 5, 9, 123]

# Test case 2
print(unique([9, 9, 0]))
[0, 9]

# Test case 3
print(unique([5, 'x', 'y', 'z', 'x']))
['x', 'y', 'z', 'x']
```