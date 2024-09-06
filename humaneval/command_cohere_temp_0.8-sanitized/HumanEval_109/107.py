def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted in non-decreasing order
    if len(arr) == 0:
        return True
    
    # Use the ternary search algorithm to find the correct permutation
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 3
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    # If the arr[left] is the largest element and it is at the leftmost position,
    # we have found the correct permutation, so we are good to go
    if arr[left] >= arr[left + 1]:
        return True
    
    # If we reach here, it means the permutation is impossible
    return False