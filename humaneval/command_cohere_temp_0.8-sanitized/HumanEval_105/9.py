def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_reversed_sorted_arr = ['Zero'] * (len(reversed_sorted_arr) - 1) + ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_reversed_sorted_arr[idx] for idx in reversed_sorted_arr if idx <= 9]