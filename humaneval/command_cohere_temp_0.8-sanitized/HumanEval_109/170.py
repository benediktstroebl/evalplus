def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # If the length of the sorted array is less than the length of the original array,
    # it's not possible to achieve a non-decreasing order
    if len(sorted_arr) < len(arr):
        return False

    # Iterate through the original array and compare with the sorted and unique array
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            return False

    # If we reach this point, it's possible to achieve non-decreasing order by shifting
    return True