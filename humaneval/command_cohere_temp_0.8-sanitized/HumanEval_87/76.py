def get_row(lst, x):
    result = []
    for row in lst:
        row_counter = 0
        for col in row:
            if row_counter == x:
                result.append((row_counter, col))
            row_counter += 1
    result.sort(key = lambda x: (x[0], -x[1]))
    return result