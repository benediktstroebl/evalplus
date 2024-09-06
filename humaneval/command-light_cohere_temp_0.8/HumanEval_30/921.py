```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
tests = [
    "Input: [-1, 2, -4, 5, 6]
    Output: [2, 5, 6]
    "Input: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]"
    Output: [5, 3, 2, 3, 9, 123, 1]
]

def test_function(t):
    result = get_positive(t['input'])
    assert result == t['expected'],
    print("Test passed:", result=", result)

# Run tests
for item in tests:
    test_function(item)
```