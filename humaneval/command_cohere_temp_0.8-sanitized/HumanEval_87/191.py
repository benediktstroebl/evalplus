def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((i, len(row_x)))
            result.extend((i, col) for col in sorted(row_x))
    return result