def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[idx] for idx in reversed_digits]