def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_x = [column for column in row if column == x]
        if row_x: 
            result.append((i, len(row_x)))
            result.extend((i, index) for index in enumerate(row_x))
    return result