def pluck(arr):
    # Calculate the smallest even value and its index
    even_value = min(x for x in arr if x % 2 == 0)
    indices = [i for i, val in enumerate(arr) if val == even_value]
    smallest_index = min(indices, key=lambda x: x[0])[0]

    return [even_value, smallest_index]