def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    return [name for num in reversed_sorted_arr for name in {'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'}[num]] if reversed_sorted_arr else []