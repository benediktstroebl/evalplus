```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test cases 

test_values = [
    [], 
    ['a', 3, 'c', (1), {}],
    [1, 2, 3, 'abc', []]
]

test_results = []
for test_value in test_values:
    test_results.append(filter_integers(test_value))

print("Test Results:")
for result in test_results:
    print(result)
```