```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_num, col_num))
                break
        row_num += 1
    result.sort(key=lambda x: (x[1], x[0]))
    return result
```

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated element by element. Whenever the desired value `x` is encountered, a tuple `(row_num, col_num)` is created, where `row_num` indicates the row index and `col_num` indicates the column index. The tuple is then appended to the `result` list. After traversal throughout the entire list, the `result` list is sorted in the manner described in the prompt by using a lambda function as the sorting key. The lambda function sorts the tuples first by the column index in ascending order and then by the row index in ascending order. Finally, the sorted list of tuples is returned.