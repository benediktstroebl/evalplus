```python
def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

The code iterates through each nested list in the `matrix`, and within each list, it checks if the value `x` exists and gathers all coordinates (`row`, `column`) where it finds this value. The found coordinates are then sorted first by the `row` in ascending order and then by the `column` in descending order, ensuring that the output is consistent with the expected format. 

Let's put this code to the test with examples:
```python
test = [
    ([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1),
    ([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 2),
    ([[1], [1, 2, 3], [1, 2, 3, 4]], 3),
]

for args, x in test:
    print(f'Input: {args}, Find: {x}')
    assert get_row(args, x) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
```