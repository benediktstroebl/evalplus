def get_row(matrix, x):
    row_dict = {} 
    result = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == x:
                if (i, j) not in row_dict:
                    row_dict[(i, j)] = True
                    result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result