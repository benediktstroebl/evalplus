def get_row(lst, x):
    result = []
    for row in lst:
        if x in row: 
            result.append((idx, len(row)))
            result.sort(key = lambda x: x[1])
    return result