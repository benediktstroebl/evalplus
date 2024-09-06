def pluck(arr):
    # Sort the list and remove odd numbers
    even_indices = [i for i, n in enumerate(arr) if n % 2 == 0]
    if even_indices:
        return [min(arr[even_indices]), even_indices.index(min(arr[even_indices]))]
    else:
        return []