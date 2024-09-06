def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if any element is positioned at the 0th index after a single right shift.
    if arr[0] == arr[-1]:
        return True
    
    # Check if any adjacent elements are equal.
    # If yes, we can optimally sort the array after a single right shift.
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return True
    
    # Check if the first half and the second half of the array are sorted.
    mid = len(arr) // 2
    if arr[:mid] == arr[mid:]:
        return True
    
    # If none of the above conditions are met, we need to swap elements in order to sort the array.
    # However, due to the exclusive use of right shifts, this is impossible to achieve.
    return False