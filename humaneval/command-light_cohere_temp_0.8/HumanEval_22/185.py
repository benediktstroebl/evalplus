```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', }
values2 = [3.14, 5]
result1 = filter_integers(values1)
result2 = filter_integers(values2)

print(result1)  # Expected output: [1, 2, 3]
print(result2)  # Expected output: [3.14, 5]
```