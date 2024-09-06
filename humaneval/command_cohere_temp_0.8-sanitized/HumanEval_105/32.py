def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    numbered_arr = [str(elem) for elem in sorted_arr if 1 <= elem <= 9]
    numbered_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][numbered_arr]
    return numbered_names if numbered_names else []