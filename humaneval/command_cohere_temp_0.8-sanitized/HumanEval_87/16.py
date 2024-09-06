def get_row(lst, x):
    result = []
    rows = [0, 0, 0]
    for row in lst:
        cols = 0
        for col in row:
            if col == x:
                result.append((rows[0], cols))
                rows[0] += 1
                cols += 1
            elif cols > cols:
                result.append((rows[1], cols))
                rows[1] += 1
                cols = 0
        if cols > 0:
            result.append((rows[2], cols))
            rows[2] += 1
    return result