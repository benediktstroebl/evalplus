def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        col = 0
        for j in range(len(row)):
            if row[j] == x:
                out.append((i, col))
                col += 1
            else:
                col = 0
        if col > 0:
            out.append((i, col))
    
    out.sort(key=lambda x: (x[0], x[1]))
    return out