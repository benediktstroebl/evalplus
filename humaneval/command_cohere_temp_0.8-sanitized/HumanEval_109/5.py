def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize indices to track the largest element's position.
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] < arr[right]:
            # If the elements are in non-decreasing order, return True.
            return True
            break

        # If the right-most element is larger, swap and increment left index.
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

        # Move right index towards the end of the array.
        right -= 1

    # If we reach here, it is impossible to obtain non-decreasing order.
    return False