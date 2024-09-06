```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, None]]
    
# Test cases
tests = [[]]
for _ in range(5):
    test_cases = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [-5, -3, -5, -2, -3, -3, -9, -0, -123],
    ]
    tests.append(unique(test_cases))

# Verify results against test cases
for test in tests:
    assert test == test_cases, f"Incorrect result: {test}"
```