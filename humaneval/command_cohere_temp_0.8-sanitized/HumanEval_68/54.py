def pluck(arr):
    if not arr:
        return []
    
    # Use a set to filter out even values and find the minimum
    even_values = {x for x in arr if x % 2 == 0}
    min_even_value = min(even_values)
    
    # Use a dictionary to store indices of even values for quick lookup
    even_indices = {x: i for i, x in enumerate(arr) if x % 2 == 0}
    
    # If there's a tie in even values, choose the one with the smaller index
    smallest_index = next(i for i, x in even_indices.items() if x == min_even_value)
    
    return [min_even_value, smallest_index]
arr = [4, 2, 3]