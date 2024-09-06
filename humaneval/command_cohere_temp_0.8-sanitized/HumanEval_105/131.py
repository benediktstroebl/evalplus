def by_length(arr):
    validated_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(validated_arr)
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_sorted_arr] if reversed_sorted_arr else []