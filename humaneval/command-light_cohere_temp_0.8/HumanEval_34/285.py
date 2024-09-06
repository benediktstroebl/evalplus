```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

#Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c'],
    ['a', 'b', 'c', 'd'],
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Expected: {', end='')
    print(test_case)
    print("}")
    print("Actual:", end='')
    print(actual)
    print("}")
```