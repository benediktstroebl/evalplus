def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    return [names[idx] for idx, val in enumerate(filtered_sorted[::-1])]
names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
arr = [2, 1, 1, 4, 5, 8, 2, 3]