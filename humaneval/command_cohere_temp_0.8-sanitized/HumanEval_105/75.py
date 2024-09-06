def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if 1 <= x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    numbers_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [numbers_names[i] for i in reversed_sorted_arr if i >= 1 and i <= 9]