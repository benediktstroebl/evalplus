def get_row(lst, x):
    result = []
    for row in lst:
        temp = [tuple(c) for c in zip(*row)]
        temp.sort(key=lambda x: x[1])
        if x in temp:
            result.append(temp[temp.index(x)])
    result.sort(key=lambda x: x[0])
    return result