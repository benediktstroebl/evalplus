def by_length(arr):
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    if not filtered_arr:
        return []
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    result = [digit_names[num - 1] for num in reversed_arr]
    return result
