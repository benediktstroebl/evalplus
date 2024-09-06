def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_sorted = [val for val in sorted_arr if 1 <= val <= 9]
    reversed_filtered = filtered_sorted[::-1]
    result = [names[idx] for idx, num in enumerate(reversed_filtered) if num < 10]
    return result if result else []
names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]