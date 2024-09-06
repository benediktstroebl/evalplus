def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((i, len(row_x)))
            result.extend([(i, j) for j in range(len(row_x) - 1, -1, -1)])
    return result