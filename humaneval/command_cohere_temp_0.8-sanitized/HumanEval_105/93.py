def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [num for num in sorted_arr if 1 <= num <= 9]
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(filtered_sorted)