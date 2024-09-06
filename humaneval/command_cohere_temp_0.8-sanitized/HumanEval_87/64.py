def get_row(matrix, x):
    result = []
    for i, row in enumerate(matrix):
        row_len = len(row)
        if row_len > x:  # check if x exists in current row
            result.append((i, row_len))
    result.sort(key=lambda x: x[0])  # sort by row in ascending order
    result.sort(key=lambda x: x[1], reverse=True)  # sort by col in descending order
    return result