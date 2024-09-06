def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x >= 1 and x <= 9, x))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    named_arr = [["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][i-1] for i in reversed_sorted_arr if i >= 1 and i <= 9]
    return named_arr