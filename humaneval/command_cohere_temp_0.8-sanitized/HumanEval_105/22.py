def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [val for val in sorted_arr if 1 <= val <= 9]
    reversed_digits = filtered_digits[::-1]
    named_digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_digits[idx] for idx in reversed_digits]