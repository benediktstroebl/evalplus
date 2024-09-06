
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
    num_changes = 0
    front_index = 0
    back_index = len(arr) - 1
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front != back:
            num_changes += 1
            # changing front
            arr[front_index] = arr[back_index]
            # changing back
            arr[back_index] = front
            back_index -= 1
        else:
            front_index += 1
            back_index -= 1

    return num_changes
