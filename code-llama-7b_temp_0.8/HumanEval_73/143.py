
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    if len(arr) < 2:
        return 0

    # Find the index of the element in the middle of the array, and the number of elements
    # greater than the middle
    mid = len(arr) // 2
    mid_element = arr[mid]
    num_greater_mid = sum(element > mid_element for element in arr)

    # If the middle element is the smallest, we don't need to change anything
    if num_greater_mid == 0:
        return 0

    # Otherwise, we need to calculate the smaller number of elements to change to make the
    # array palindromic
    num_changes = 0
    left = 0
    right = len(arr) - 1

    while left <= mid:
        # If the left and right sides of the array are not the same, we can change the element in
        # the left side to the middle element, since it will be the same on the right side
        while arr[left] <= mid_element and left <= mid:
            left += 1
        # If the left side is greater than the middle element, change the left side to the right
        # side. Since we're iterating the left side from the middle to the end, this should only
        # happen if we've already passed the middle
        if arr[left] > mid_element and left <= mid:
            num_changes += 1
        # If the right side is smaller than the middle element, change the right side to the left
        # side. Since we're iterating the right side from the middle to the beginning, this should
        # only happen if we're still in the middle or past it
        if arr[right] < mid_element and right >= mid:
            num_changes += 1
            right -= 1

    # Since we've already done the middle element, we don't need to change it again, so we
    # need one less than the number of changes on each side
    return num_changes // 2 + num_greater_mid // 2
