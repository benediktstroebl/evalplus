
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
    # get sorted indices for array
    idx = sorted(range(len(arr)), key=lambda k: arr[k])
    # get first and last element indices
    front, back = idx[0], idx[-1]
    # get number of elements needed to make front <= back
    return len(arr) - 1 if front > back else abs(front - back)

