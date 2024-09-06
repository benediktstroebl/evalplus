def pluck(arr):
    if not arr:
        return []
    
    # Using collections to find the smallest even value and its index
    it = filter(lambda x: x % 2 == 0, arr)
    min_value, min_idx = min(it), next(iter(it))

    # Filtering the list for the smallest index value if there are multiples
    it = filter(lambda x: x == min_value, arr)
    min_idx = min(range(len(arr)), key=lambda x: arr[x] == min_value)
    
    return [min_value, min_idx]