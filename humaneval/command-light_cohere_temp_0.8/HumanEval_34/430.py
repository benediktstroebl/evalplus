```python
def unique(lst):
    """Sorts and returns unique elements from a list"""
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test cases
tests = [
    [
        ( [5, 3, 5, 2, 3, 3, 9, 0, 123], "Should return unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123]) -> [0, 2, 3, 5, 9, 123]", True),
        ( [2, 2, 3, 5, 3], "Should handle duplicate elements properly", True),
        ( [2, 3, 5, 'two', 0, 0, 5], "Should handle string and float properly", True),
    ]

for test_case, description, should_pass in tests:
    print(f"{description}\nShould {should_pass}")
    assert unique(test_case) == should_pass
```