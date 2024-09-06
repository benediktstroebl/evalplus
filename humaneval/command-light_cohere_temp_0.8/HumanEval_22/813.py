```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test the function using the same inputs as the previous problem statement
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 'a', 45, 7]))  # [10, 45]
```