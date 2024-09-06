def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x < 1 or x > 9, x))
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(sorted_arr)