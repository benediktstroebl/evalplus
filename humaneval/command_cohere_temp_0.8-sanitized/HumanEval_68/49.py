def pluck(arr):
    if not arr:
        return []
    
    # Use a set to filter out even values and find the smallest one
    even_values = {val for val in arr if val % 2 == 0}
    smallest_even_val = min(even_values)
    indices = [idx for idx, val in enumerate(arr) if val == smallest_even_val]
    
    return [[smallest_even_val, indices[0]] if indices else []]