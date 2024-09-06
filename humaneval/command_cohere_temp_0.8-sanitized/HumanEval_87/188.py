def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            temp = [(row_x.index(col), col) for col in row_x]
            temp.sort(key=lambda x: (x[1], x[0]))
            result.extend(temp)
    return result