def by_length(arr):
    sized = [x for x in arr if 1 <= x <= 9]
    sorted_sized = sorted(sized)
    reversed_sorted = sorted_sized[::-1]
    result = [f'{name}{len(sized)}' for name in reversed_sorted]
    return result if result else []