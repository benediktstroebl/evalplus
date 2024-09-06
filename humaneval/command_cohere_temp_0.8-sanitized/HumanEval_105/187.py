def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x >= 1 and x <= 9, x))
    reverse_sorted_arr = sorted(sorted_arr, reverse=True)
    named_arr = [["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"][i-1] for i in reverse_sorted_arr if i >= 1 and i <= 9]
    return named_arr if named_arr else []