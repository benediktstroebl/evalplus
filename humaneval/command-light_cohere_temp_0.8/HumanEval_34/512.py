```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not float('inf')]

# Test the function with markdown code block
# demonstrating list of numbers, strings, float('inf'), and special characters
# Each element is converted to a string for uniform comparison
tst = [5, 3, 5, 2, 3, 3, 9, 0, '123', 'abc', float('inf')]
assert unique(tst) == [0, 2, 3, 5, '123', 'abc', float('inf')]
```