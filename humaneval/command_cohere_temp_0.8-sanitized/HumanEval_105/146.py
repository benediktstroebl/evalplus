def by_length(arr):
    DIGITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    result = [DIGITS[i] for i in reversed_arr]
    return result if result else []