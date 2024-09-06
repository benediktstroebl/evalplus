def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            result.append((len(row_x), len(row_x) * 1)) 
    result.sort()
    result.sort(key=lambda x: x[1])
    return result