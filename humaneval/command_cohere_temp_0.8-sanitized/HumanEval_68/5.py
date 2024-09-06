def pluck(arr):
    even_nodes = [idx for idx, val in enumerate(arr) if val % 2 == 0]
    if not even_nodes:
        return []
    min_index = min(even_nodes)
    filtered_arr = [val for val in arr if val % 2 == 0 and val == arr[min_index]]
    return [[val, min_index] for val in filtered_arr] if filtered_arr else []