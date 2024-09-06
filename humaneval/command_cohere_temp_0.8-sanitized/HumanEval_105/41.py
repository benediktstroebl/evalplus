def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if 1 <= x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    numbered_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [numbered_names[idx] for idx in reversed_sorted_arr if idx <= 9]