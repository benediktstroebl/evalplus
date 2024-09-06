def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    sorted_arr = sorted(arr)
    reversed_sorted_arr = sorted(sorted_arr)[::-1]
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(DIGS[num - 1])
    return result