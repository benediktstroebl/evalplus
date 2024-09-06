```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
tests = {
    "Input: [-1, 2, -4, 5, 6]
    "Expected Output: [2, 5, 6]"
})

# Test suite
def test_get_positive():
    assert get_positive([]) == []
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main execution
test_get_positive()
```