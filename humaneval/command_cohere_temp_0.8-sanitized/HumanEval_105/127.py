def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = sorted(filtered_digits, reverse=True)
    named_digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [named_digits[i] for i in reversed_digits]
arr = [2, 1, 1, 4, 5, 8, 2, 3]