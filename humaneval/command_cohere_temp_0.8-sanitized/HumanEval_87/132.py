def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_match = [y for y in row if y == x]
        if row_match:
            result.append((i, len(row_match)))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result