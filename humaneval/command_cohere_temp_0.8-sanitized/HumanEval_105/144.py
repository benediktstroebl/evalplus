def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }.get
    result = [transf_map(elem) for elem in sorted_arr if elem <= 9 and elem >= 1]
    return result if result else []