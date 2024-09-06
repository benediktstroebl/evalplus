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

The nested list, `matrix`, is iterated through row by row. Within each row, the list is iterated through column by column. When the value `x` is encountered, a tuple of coordinates is created as `(row_num, column_num)`. This tuple is then appended to the `result` list. Once all rows have been searched, the tuples are sorted first by row number in ascending order and then by column number in descending order, ensuring that the output is consistent with the provided examples. 

Here is an example usage of the function for the input provided in the prompt: 
```python
print(get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1))
```

The output will be:
```
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
``` 

This is consistent with the provided example. 

The function also handles cases where the matrix or the value `x` is empty, returning an empty list in such cases. 

This solution follows the iterative approach and searches the matrix iteratively, making it suitable for large matrices. 

The function can efficiently handle the described input format and will return the coordinates of all instances of `x` in the matrix, sorted as requested.