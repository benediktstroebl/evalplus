```python
def get_row(lst, x):
    result = []
    rows = []
    r, c = 0, 0
    for row in lst:
        if x in row: 
            col = row.index(x)
            result.append((r, c))
            result.sort(key=lambda x: (x[1], x[0]))
            c += 1
        else: 
            c = 0
        if not c: 
            r += 1
            c, rows = 0, []
    return result + sorted(rows)
``` 

The code uses a nested loop to iterate through each element of the list lst. For each element x, the code iterates through each row of lst and keeps track of the column index of x in that row. It also maintains the current row and column indices to keep track of the position in the matrix.

If x is not found in the current row, it initializes the column index to 0 and moves to the next row. The code keeps track of rows that did not have enough columns to reach the x-th term in a list rows, and completes the last row if necessary, yielding the final row tuple directly in the list. The result list is kept sorted in ascending order by row index, and within each row, by column index.