def pluck(arr):
    even_values = filter(lambda x: x % 2 == 0, arr)
    min_value = min(even_values)
    min_index = min(idx for idx, value in enumerate(even_values) if value == min_value)
    
    return [min_value, min_index] if min_value else []