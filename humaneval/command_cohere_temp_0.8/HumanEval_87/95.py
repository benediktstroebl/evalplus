```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                break
        column_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))
```

The algorithm utilizes two indices, `row_index` and `column_index`, to efficiently traverse the nested list `matrix`. Upon encountering a list element matching the target `x`, the algorithm constructs a tuple representing the row and column indices of the element, appends it to the `result` list, and moves to the next element in the same row. The final output is sorted first by row in ascending order and then by column in descending order, ensuring the coordinates are correctly organized.

The code includes an example and corresponding test cases to validate its correctness:
```python
# Example usage
matrix = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1]
]
x = 1
expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row(matrix, x))
assert get_row(matrix, x) == expected

# Edge cases
print(get_row([], 1))
assert get_row([], 1) == []

print(get_row([[], [1], [1, 2, 3]], 3))
assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
```