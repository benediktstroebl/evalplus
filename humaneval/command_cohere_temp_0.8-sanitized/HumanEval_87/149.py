def get_row(lst, x):
    result = []
    for row in lst:
        temp = [coord for coord in row if coord == x]
        temp.sort(key=lambda x: x[1])
        result.append(temp)
    return result