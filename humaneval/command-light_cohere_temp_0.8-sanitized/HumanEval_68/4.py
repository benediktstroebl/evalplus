def pluck(arr):
    if not arr or len(arr) == 0:
        return []

    values = [n for n in arr if n % 2 == 0]
    if len(values) == 0:
        return []
    
    smallest_value = min(values)
    smallest_index = values.index(smallest_value)

    return [smallest_value, smallest_index]