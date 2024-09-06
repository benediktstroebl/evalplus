def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    numbered_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [numbered_names[idx] for idx in reversed_sorted_arr if idx <= 9]
    return result if result else []