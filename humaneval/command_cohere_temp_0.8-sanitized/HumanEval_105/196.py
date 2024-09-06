def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x < 1 or x > 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name_digit(x) for x in reversed_sorted_arr]
    return result
def name_digit(num):
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return names[num] if 0 <= num <= 8 else ''