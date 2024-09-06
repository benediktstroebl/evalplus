def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    return [name for i, name in enumerate(
        ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"], 1)
        if i == reversed_sorted_arr[0]]