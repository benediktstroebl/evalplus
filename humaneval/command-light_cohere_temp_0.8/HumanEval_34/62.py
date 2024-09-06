```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 20, 30, 40, 50, 60, 70, 80, 90],
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Expected unique list: {', ' '.join(map(str, actual))[:-len(actual)] + [']')
    print("Got unique list:", ', end='')
    print(f"{' '.join(map(str, actual))}"[:len(actual)] + [''])
    assert actual == [0, 2, 3, 5, 9, 123]]
```
This code implements a unique function that removes duplicate elements from the input list and returns a new list with unique values. The test cases ensure that the expected output is the list with all unique elements.