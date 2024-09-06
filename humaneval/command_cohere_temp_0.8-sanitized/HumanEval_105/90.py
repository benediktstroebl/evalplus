def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    if not arr:
        return []
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted_arr[::-1]
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(DIGS[num - 1])
    return result