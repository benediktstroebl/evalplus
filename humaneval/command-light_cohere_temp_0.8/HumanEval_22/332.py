```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

#Test the function with some examples
values1 = [1, 2, 3, 'abc', {}, [0, 1, 2)]
print(filter_integers(values1))  # Output: [1, 2, 3]

values2 = [1, 2, 3, 4, 5, 'abc', None)
print(filter_integers(values2))  # Output: [1, 2, 3, 4, 5]

values3 = [1, 2, 3.b, 0]
print(filter_integers(values3))  # Output: [1, 2, 3, int]
```