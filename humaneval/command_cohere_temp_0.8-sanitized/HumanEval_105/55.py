def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 1 + 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    numbered_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [numbered_names[int(x) - 1] for x in reversed_sorted_arr if x <= 9]
    return result if result else []