```python
def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [
    [], 
    [],
    ['a', 3, 'four', 'five', 1],
    [1, 2, 3, 'abc', {}],
]

test_results = []
for values in test_values:
    test_results.push(filter_integers(values))

# Print the results
print("Test Results:") * ", end='')
for result in test_results:
    print(", ".join(result))
```