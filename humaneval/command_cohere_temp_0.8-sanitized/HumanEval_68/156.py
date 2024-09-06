def pluck(arr):
    if not arr:
        return []

    # Use a set to filter out even values and find the minimum
    even_values = {x for x in arr if x % 2 == 0}
    min_even_value = min(even_values)
    min_index = arr.index(min_even_value)

    return [min_even_value, min_index]