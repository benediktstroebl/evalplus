def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((idx, len(row_x)))
            result.sort(key=lambda x: (x[0], -x[1]))
    return result