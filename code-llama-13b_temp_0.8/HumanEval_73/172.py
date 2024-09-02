
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
    if not arr:
        return 0
    if len(arr) == 1:
        return 0

    left = 0
    right = len(arr) - 1
    num_changes = 0

    while left < right:
        while arr[left] == arr[right]:
            left += 1
            right -= 1
            if left >= right:
                return num_changes

        while arr[left] != arr[right]:
            # always change the smallest number to the largest number
            if arr[left] < arr[right]:
                new_value = max(arr) + 1
                if new_value > arr[right]:
                    # if we are above the number we want to change, we need to decrement
                    arr[left] = new_value
                    num_changes += 1
                    left += 1
                else:
                    # otherwise we can change it to any other number
                    arr[left] = arr[right]
                    num_changes += 1
                    left += 1
                    right -= 1

            else:
                # always change the smallest number to the largest number
                if arr[right] < arr[left]:
                    # if we are above the number we want to change, we need to decrement
                    arr[right] = max(arr) + 1
                    num_changes += 1
                    right -= 1
                else:
                    # otherwise we can change it to any other number
                    arr[right] = arr[left]
                    num_changes += 1
                    left += 1
                    right -= 1

    return num_changes

