def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [Names[int(i)] for i in sorted_arr if 1 <= int(i) <= 9]
    return named_arr