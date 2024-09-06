def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]

    # Iterate over the array to compare elements
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            if arr[i] > last or (arr[i] == last and i > first):
                return True
        elif arr[i] < arr[i - 1]:
            if arr[i] < first or (arr[i] == first and i < last):
                return True
        elif arr[i] == arr[i - 1]:
            if i - 1 > first and i < last:
                return True

    return False