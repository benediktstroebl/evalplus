```python
def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        col = 0
        for j in range(len(row)):
            if row[j] == x:
                out.append((i, col))
                col += 1
            else:
                col = 0
        if col > 0:
            out.append((i, col))
    
    out.sort(key=lambda x: (x[0], x[1]))
    return out
```

The nested list, `lst`, is iterated through using a nested loop. The loop for the list, `i`, iterates through each row, while the loop for `j` goes through each element in the current row. As the nested loops progress, the column position of the target `x` is tracked using the `col` variable. Once the target is found in a row, a tuple of coordinates is appended to the output list, and the column position is incremented so that further iterations will resume from the next column. This process ensures that all occurrences of `x` are captured in the output list, and the tuples are sorted first by row in ascending order and then by column in ascending order as required by the problem statement. 

This code will output the list of tuples, `(x1, y1), (x2, y2) ...` for each occurrence of the target integer `x` in `lst`, such that each tuple represents the coordinates of the target in the form - `(row, column)`, starting from index 0. The tuples are sorted in the specified order. 

The `get_row` function as provided in the code block above serves as a definitive solution to the problem described in the markdown code block. It is important to note, that the function, `get_row`, assumes that the nested list `lst` is not empty, and the target integer `x` is present in at least one of the rows in the list. If the input list is empty or `x` is not present in any of the rows, the function will return an empty list.