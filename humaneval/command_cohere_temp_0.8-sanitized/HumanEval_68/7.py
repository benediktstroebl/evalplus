def pluck(arr):
    if not arr:
        return []

    # Use a default value of 2 for index to handle negative values or values greater than array length
    indices = collections.Counter(arr)
    min_index = min(indices.values())

    # Filter only even values and get the minimum value
    filtered = [val for val in arr if val % 2 == 0]
    min_even = min(filtered) if filtered else 2

    return [min_even, min_index] if min_even in filtered else []