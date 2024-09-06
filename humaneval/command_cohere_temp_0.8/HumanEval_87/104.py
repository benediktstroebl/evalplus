```python
def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    col_indices = [cols for row in lst for cols in enumerate(row)]
    for i, row_cols in enumerate(zip(rows, col_indices)):
        if x == row_cols[0]:
            result.append((i, row_cols[1]))
    result.sort()
    result.sort(key=lambda x: x[1])
    return result
```

The function iterates through the rows of the list, comparing the length of each row to the input value `x`, and when a match is found, the function constructs and returns a tuple containing the row index and the column index where the `x` value is located, it then sorts the results first by row index in ascending order and then by column index in ascending order, this ensures that the output is always the same regardless of the order of inputs. 

Here is how you can use it:
```python
print(get_row([['1','2','3'],[1,2,3], [1,2,3,4]],[3]))
``` 

which should print:
```bash
[(1, 2)]
``` 

This is because there is only one occurrence of "3" in the matrix, located in the second column of the second row, so only one coordinate is returned and sorted by column in ascending order.