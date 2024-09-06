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