def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates
    return sum(1 for i in range(len(arr)) for j in range(len(arr)-1-i) if arr[i] != arr[j])