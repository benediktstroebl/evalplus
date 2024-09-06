def by_length(arr):
    DIGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted_arr[::-1]
    result = []
    for num in reversed_sorted_arr:
        if num in DIGS:
            result.append(DIGS[num])
    return result if result else []