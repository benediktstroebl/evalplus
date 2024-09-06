```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in []]

# Test cases
tests = [
    [
        [],
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        ['a', 'a', 'b', 'c'],
        ['a', 'aa', 'b', 'aa', 'c', 'xx']
    ]
)

for test_case in tests:
    actual = unique(test_case)
    print(f"Expected: {', ', '.join(map(str, set(test_case)))})
    print("Actual:",', ' '.join(map(str, actual)))
```