def pluck(arr):
    # Define a nested list to hold smallest even values and their indices
    result = []
    arr_len = len(arr)
    nested = [[abs(n-2), i] for i, n in enumerate(arr) if n >= 2]
    # If the nested list is empty, return an empty list
    if not nested:
        return []
    # Sort the nested list by values (even nodes) and then by indices (smallest index first)
    nested.sort(key=lambda x: [x[0], x[1]])
    # Fetch the node with the smallest index value
    return [nested[0][0], nested[0][1]]