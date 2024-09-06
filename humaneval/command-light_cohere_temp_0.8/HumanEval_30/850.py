```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with several lists of different sizes and types
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123])
assert(get_positive([5, 'asdfdfdsadfdsadfds', -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 2, 3, 9])
assert(get_positive([True]) == [True])
assert(get_positive([1, 2, 3, -100])) == [1, 2, 3]
```