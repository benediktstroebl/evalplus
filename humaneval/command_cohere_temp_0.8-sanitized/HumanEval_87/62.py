def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = []
    for row in lst:
        temp = [i for i in row]
        cols.append(temp)
        result.append(sorted(enumerate(temp), key=lambda x: (x[1], x[0])))
    result = sorted(result, key=lambda x: (x[0], len(x[1])))
    return [coord for coord in result if coord[0] == x]