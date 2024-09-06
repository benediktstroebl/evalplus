def pluck(arr):
    if not arr:
        return []

    # Use a default value of 2 for index to handle even and odd cases
    min_value = min(arr, key=lambda x: (x, arr.index(x)))
    
    # Filter even values and find the minimum index
    even_values = [x for x in arr if x % 2 == 0]
    min_index = min(even_values, key=arr.index)
    
    return [min_value, min_index]