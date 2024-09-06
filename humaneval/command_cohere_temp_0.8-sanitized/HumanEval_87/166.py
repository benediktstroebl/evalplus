def get_row(lst, x):
    result = []
    for row in lst:
        temp = [tuple(e) for e in enumerate(row)]
        temp.sort(key=lambda x: x[1])
        temp.sort(key=lambda x: x[0])
        if x in temp[0][0]:
            result.extend(temp)
    return result