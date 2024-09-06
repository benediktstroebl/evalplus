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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated element by element. Whenever the desired value `x` is encountered, a tuple `(row_num, col_num)` is created, indicating the row and column number of the element. This tuple is appended to the `result` list. After iterating through all rows and columns, the tuples within `result` are sorted first by the column number in ascending order and then by the row number in ascending order, ensuring the elements are sorted by columns within each row. Finally, the sorted list of tuples is returned. 

This approach ensures that the elements are correctly identified and sorted in the output list of tuples.