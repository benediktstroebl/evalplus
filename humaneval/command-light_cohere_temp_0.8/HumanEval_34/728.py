```python
def unique(l: list):
    return list(set(l))

# Test the unique function with a list of elements
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Use the unique function to get sorted unique elements
result = unique(test_list)

# Validate the result
if result != [0, 2, 3, 5, 9, 123]:
    raise ValueError("Expected [0, 2, 3, 5, 9, 123], got %s" % result)

print("Unique elements:", result)
```