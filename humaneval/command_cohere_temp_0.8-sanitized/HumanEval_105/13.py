def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    num_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(num_names[num - 1])
    return result