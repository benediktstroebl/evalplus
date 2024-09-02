
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
    n = len(arr)
    front = 0
    back = n - 1
    # If it is already palindromic, return 0
    if is_palindromic(arr):
        return 0
    # If the first number is smaller than the last,
    # reverse the second half and compare each number
    # from the front and back
    if arr[front] < arr[back]:
        while front < n - 1 and arr[front] < arr[front + 1]:
            front += 1

        while back > 0 and arr[back] < arr[back - 1]:
            back -= 1

    # Else the first number is larger than the last
    # reverse the first half and compare each number
    # from the front and back
    else:
        while front < n - 1 and arr[front] > arr[front + 1]:
            front += 1

        while back > 0 and arr[back] > arr[back - 1]:
            back -= 1

    # Return the difference between the front and back,
    # that is the number of elements to change
    return n - max(front + 1, back)

