
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
    min_changes = 0
    front = 0
    back = len(arr) - 1

    while front < back:
        # if the two elements are not equal,
        # increment the counter and move both front and back
        if arr[front] != arr[back]:
            min_changes += 1
            if front - 1 >= 0 and arr[front - 1] == arr[back]:
                front -= 1
            if back + 1 <= len(arr) - 1 and arr[front] == arr[back + 1]:
                back += 1
        else:
            front += 1
            back -= 1

    return min_changes
