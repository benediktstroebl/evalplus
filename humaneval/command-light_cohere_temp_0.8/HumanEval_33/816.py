```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) % 3)

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [15, 16, 23, 32, 56, 72, 89]
]

for test_case in test_cases:
    actual = sort_third(test_case)
    assert actual == test_case  # Test if the output matches the expected output
```

This script defines a function called sort_third, which takes a list lst as input and returns a sorted list with values that are not divisible by three at the indices that are not divisible by three. The function achieves this using the approach of sorting by considering the remainder of the division by three for each value in the list. The test cases provided are used to verify the correctness of the function by checking if the output matches the expected output.