```python
def unique(l: list):
    return list(set(l))

# Test the unique function with a list of elements
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Run the test and print the result
print(test_unique())
```