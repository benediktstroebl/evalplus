def smallest_change(arr):
    num_changes = float('inf')
    for i in range(1, len(arr)):
        mirror_index = len(arr) - i
        if arr[i] != arr[mirror_index]:
            num_changes = min(num_changes, 2)
    return num_changes if num_changes == float('inf') else num_changes + 1