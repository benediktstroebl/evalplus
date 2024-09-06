def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Check if the array is already sorted
    if arr[0] >= arr[1]:
        return True

    # Check if the last element can 'bubble up' to the correct position
    index = arr.index(min(arr))
    if arr[index] >= arr[index-1]:
        return move_one_ball(arr[:index-1] + arr[index:])

    # Otherwise, it's not possible to sort the array
    return False