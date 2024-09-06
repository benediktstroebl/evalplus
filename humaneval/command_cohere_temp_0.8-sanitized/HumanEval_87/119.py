def get_row(lst, x):
    result = []
    for row in lst:
        for col in row:
            if col == x:
                result.append((row, col))
    result.sort(key=lambda x: (x[0] or 0, x[1]))
    return result