```python
def add_elements(arr, k):
    # Your implementation here
    return sum(x for x in arr[:k] if len(str(x)) <= 2)

# Test the function with sample inputs
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
assert result == 24

# Test again with modified inputs (to pass different test cases)
arr2 = [123,123,123]
k2 = 3
result2 = add_elements(arr2, k2)
assert result2 == 67
```