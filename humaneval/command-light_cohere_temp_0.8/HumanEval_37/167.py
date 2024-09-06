```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

#Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [7, 8, 9]
]

for test_case in test_cases:
    actual = sort_even(test_case)
    assert actual == [3, 6, 5, 4]
```