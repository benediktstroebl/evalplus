def pluck(arr):
    if not arr:
        return []
    
    # Use a set to filter out even values and find the minimum
    even_values = {val for val in arr if val % 2 == 0}
    min_even_value = min(even_values)
    
    # Use a dictionary to store indices of even values and find the minimum index
    index_dict = {val: idx for idx, val in enumerate(arr) if val % 2 == 0}
    min_index = min(index_dict, key=index_dict.get)
    
    return [min_even_value, min_index]