
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    max_elem = max(arr)
    hash_table = dict(zip(arr, [0] * len(arr)))
    total = sum(arr)
    if total % 2 == 1:
        return -1
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] <= max_elem:
            hash_table[arr[i]] += 1
    if hash_table[arr[-1]] == 1:
        hash_table.pop(arr[-1])
    for key, value in hash_table.items():
        if key < total - key:
            if key in hash_table:
                return len(arr) - 1
            else:
                return hash_table.get(total - key)
    return -1
    
