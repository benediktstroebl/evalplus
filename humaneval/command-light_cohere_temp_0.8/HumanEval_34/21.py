```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not  <  len(seen)]

# Test cases
unique_test = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Unique element list:", unique_test)

seen = set()
print("Expected output:", [0, 2, 3, 5, 9, 123])
print("Result:", unique(unique_test))
```