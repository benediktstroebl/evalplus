def pluck(arr):
    # Filter even values and sort by index (smallest first)
    even_values = [x for x in arr if x % 2 == 0]
    if not even_values:
        return []
    return [min(even_values), even_values.index(min(even_values))]