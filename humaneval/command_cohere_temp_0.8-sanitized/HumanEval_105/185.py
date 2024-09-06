def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if 1 <= x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_arr = [name_of_digit(x) for x in reversed_sorted_arr]
    return named_arr
def name_of_digit(x):
    if 1 <= x <= 9:
        return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][x - 1]
    else:
        return ""