def get_row(lst, x):
    result = []
    rows = [0, 0, 0]
    for i in range(0, len(lst)):
        row = lst[i]
        cols = len(row)
        if cols == x:
            result.append((rows[0], cols))
            rows[0] += 1
        elif cols > x:
            result.append((rows[1], cols))
            rows[1] += 1
        else:
            result.append((rows[2], cols))
            rows[2] += 1
    result.sort(key=lambda x: (x[0], -x[1]))
    return result