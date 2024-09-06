def get_row(lst, x):
    result = []
    for row in lst:
        row_counter = 0
        for val in row:
            if val == x:
                result.append((row_counter, row_counter))
                row_counter += 1
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result