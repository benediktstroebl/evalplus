def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_match = [col for col in row if col == x]
        if row_match:
            result.append((i, len(row_match)))
            result.sort(key=lambda x: (x[0], -x[1]))
    return result