Here's the code to solve your problem:
```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in []]

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [1, 2, 3, 4, 5, 6, 7],
    ['a', 'a', 'b', 'c'],
    [1, 2, 3, 4, 5, 6, 7],
    [(), True, (), 1, 2, 3, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]

for test_case in tests:
    actual_result = unique(test_case)
    expected_result = [0, 2, 3, 5, 9, 123]
    print(f"Test {i+1}: actual={actual_result}, expected={expected_result}")
```

Please, you can use this `unique` function in your code to get the unique elements from a list.