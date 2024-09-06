def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    numbered_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [numbered_names[i] if i < len(numbered_names) else '' for i in reversed_sorted_arr]