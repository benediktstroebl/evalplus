def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = [max(row) for row in lst]
    m = len(rows)
    n = len(cols)
    for i in range(m):
        for j in range(n):
            if rows[i] == x:
                result.append((i, cols[j]))
    result.sort(key=lambda x: (x[1], x[0]))
    return result