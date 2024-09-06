```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not == 0]

# Test cases
tests = {
    'Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]
    'Output expected: [0, 2, 3, 5, 9, 123]'
})

# Test function
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Run the test and print the result
test_unique()
 ```