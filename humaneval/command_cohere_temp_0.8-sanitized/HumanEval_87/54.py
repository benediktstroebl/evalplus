def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_index + 1, col_index + 1))
                break
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))