```python
def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            result.append((idx, len(row)))
            rows.append(row)
    result.sort(key=lambda x: (x[0], -x[1]))
    rows = sorted(rows, key=lambda x: x.index(x))
    return [(idx, len(row)) for idx, row in zip(rows, result)]
```

The function iterates through each row in the list and checks if the `x` value is present in the row. If it is, a tuple of the index of the row and the number of columns in the row is appended to the `result` list. The `result` list is then sorted first by the index of the row in ascending order and then by the number of columns in descending order. Finally, the `result` list is zipped with the `rows` list to return the final list of tuples. 

The test cases are as follows:
```python
test_cases = [
    ([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1, [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]),
    ([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 2, [(1, 4), (0, 0), (2, 5), (1, 0)]),
    ([[], [1], [1, 2, 3]], 3, [(2, 2)])
]

for test_case, x, expected in test_cases:
    assert get_row(test_case, x) == expected
```

The tests verify the correct output for various inputs, including edge cases, and ensure that the output is equivalent to the expected output.