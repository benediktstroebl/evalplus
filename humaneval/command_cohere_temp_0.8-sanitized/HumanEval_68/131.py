from heapq import heappop, heappush
def pluck(arr):
    # initialize empty heap with the first even value found or raise Exception
    even_values = []
    try:
        heappush(even_values, [2, 1])  # pair of (value, index)
        for i, value in enumerate(arr):
            if value % 2 == 0:
                heappush(even_values, [value, i]) 
    except Exception as e:
        return [], 0
    
    # retrieve the minimum even value and its index
    min_value, min_index = heappop(even_values)
    return [min_value, min_index], len(even_values)