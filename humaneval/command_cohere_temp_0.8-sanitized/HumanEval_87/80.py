def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            temp = []
            for i, col in enumerate(row):
                if col == x:
                    temp.append((i+1, len(row_x[0])))
            result.extend(sorted(temp, key=lambda x: x[1]))
    return result