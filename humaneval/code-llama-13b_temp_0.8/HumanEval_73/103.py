
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
    if len(arr) == 0 or len(arr) == 1:
        return 0

    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 1
        return 0

    left, right = 0, len(arr) - 1
    count = 0
    left_front, right_front = 0, 0

    while left < right:
        if arr[left] != arr[right]:
            count += 1

            # Now we will check for left_front and right_front.
            # We will find which element is to be changed to make the array palindromic.
            # Since we are changing one element to make the array palindromic, we can't repeat
            # the same element to make the array palindromic.
            # For example: arr = [1,2,2,3,2,1],  here we can't change the second 2 and make the array
            # palindromic. Instead we will change 3.
            if left > 0 and arr[left - 1] == arr[right]:
                left_front += 1
                left -= 1
            elif right < len(arr) - 1 and arr[right + 1] == arr[left]:
                right_front += 1
                right += 1
            else:
                return -1
        else:
            left += 1
            right -= 1

    if count > 1 and left_front > 0 and right_front > 0:
        return count - 1
    else:
        return count

