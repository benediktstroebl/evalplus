def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    return [names[idx] for idx, val in enumerate(filtered_sorted[::-1]) if val <= 9]
names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]