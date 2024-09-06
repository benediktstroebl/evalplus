def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for num in reversed_digits:
        names.append(num_to_name[num])
    return names if names else []
def num_to_name(digit):
    digit_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return digit_names[digit] if 0 <= digit <= 8 else ''
arr = [2, 1, 1, 4, 5, 8, 2, 3]