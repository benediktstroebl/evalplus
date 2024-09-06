def pluck(arr):
    even, odd = partition_by_parity(arr)
    if not even:
        return []
    return min_element_by_index(even)
def partition_by_parity(arr):
    # Split array into even and odd values
    return (arr[i:i+2] for i in range(0, len(arr), 2)), arr[1::2]
def min_element_by_index(arr):
    # Return the minimum even value and its index
    return [min(arr), min(range(len(arr)), key=lambda i: arr[i])]