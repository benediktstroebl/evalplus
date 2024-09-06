def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x >= 1 and x <= 9, x))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    numbered_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [numbered_names[i] for i in reversed_sorted_arr if i >= 1 and i <= 9]
arr = [2, 1, 1, 4, 5, 8, 2, 3]