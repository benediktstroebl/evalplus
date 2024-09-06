```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test suite
test_get_positive = """
def test_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

def test_negative():
    assert not get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

test_positive()
"""

# Main script
if __name__ == "__main__":
    test_get_positive()
```