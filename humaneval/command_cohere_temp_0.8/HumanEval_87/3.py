```python
def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_num, j))
                break  # append the current coordinate and break to start with the next row
    result.sort(key=lambda x: (x[0] + 1, -x[1] + 1))
    return result
```

The code works by first using two nested loops to go through each element in each row of the matrix. When a match is found, a tuple (row number, column number) is created and added to the `result` list. After all rows have been processed, the entries in the list are sorted first by row number (in ascending order), and then by column number (in descending order), using a custom sorting key. Finally, the `result` list is returned.

This solution assumes that the input list matrix is not empty and the given value x is present in at least one row of the matrix. If these assumptions are not met, the function will raise an exception or return an empty list, depending on the situation. 

This solution is concise and efficient, but it's worth adding some comments for better code readability and maintainability. Below is a slightly modified version of the code with comments:
```python
def get_row(matrix, x):
    # Initialize an empty list to store the coordinates (row, column) where the value x is found.
    result = []
    
    # Loop through each row in the matrix.
    for row_num, row in enumerate(matrix):
        # Loop through each element in the current row.
        for j, val in enumerate(row):
            # If the current element is equal to the given value x.
            if val == x:
                # Append the coordinate (row_num, j) to the result list.
                result.append((row_num, j))
                break  # Append the current coordinate and break the inner loop to move to the next row.
    
    # Sort the result list based on the row number (ascending) and column number (descending).
    result.sort(key=lambda x: (x[0] + 1, -x[1] + 1))
    
    # Return the sorted result.
    return result
```