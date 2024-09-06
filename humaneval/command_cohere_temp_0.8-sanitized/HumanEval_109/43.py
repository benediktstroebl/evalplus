def move_one_ball(arr):
    # if the array is empty, it is possible to sort it in non-decreasing order
    if not arr:
        return True

    # check if the last element is the smallest and all other elements are greater
    # if so, it is possible to sort by moving the last element to the front
    if arr[-1] < arr[0] and all(x > arr[0] for x in arr[1:]):
        return True

    # check if the last element is the largest and all other elements are smaller
    # if so, it is possible to sort by moving the last element to the front
    if arr[-1] > arr[0] and all(x < arr[0] for x in arr[1:]):
        return True

    # check if the last element is the middle element and some elements are smaller
    # and some elements are larger
    if arr[-1] == arr[0] and all(x != arr[0] for x in arr[1:]):
        return True

    return False