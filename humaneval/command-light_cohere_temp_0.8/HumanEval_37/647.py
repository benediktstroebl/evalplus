```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x +1))

# Test the function with a list of numbers
# Expected Output: [3, 6, 5, 4]
l = [5, 6, 3, 4]
result = sort_even(l)
assert result == l

# Test the function with a list of strings
# Expected Output: ['con', 'doc', 'cat']
l = ['con', 'doc', 'cat']
result = sort_even(l)
assert result == l
```