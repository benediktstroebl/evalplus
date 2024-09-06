def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array and determine the largest index i such that arr[i] == max(arr).
    sorted_arr = sorted(arr)
    max_idx = sorted_arr.index(max(arr))

    # Calculate the number of shifts needed to move the largest element to the first position.
    num_shifts = len(arr) - max_idx - 1

    # Reverse the entire array and then shift the maximum element to the first position.
    return move_one_ball(arr[num_shifts:]+[arr[0]])