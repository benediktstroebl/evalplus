```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
print(filter_integers(['a', 3.14, 5]))  # Output: [5]

# Test case 2
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]

# Test case 3
print(filter_integers([10, 2, '20', 3.14, 5]))  # Output: [10, 2, 3. nested in int range])
```