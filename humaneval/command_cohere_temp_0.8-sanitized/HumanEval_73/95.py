def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates
    return sum([1 for i in range(len(arr)) for j in range(i, len(arr)) if arr[i] != arr[j]])