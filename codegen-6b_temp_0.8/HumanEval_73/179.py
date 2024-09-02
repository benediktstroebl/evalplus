
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
    # Initialize start elements
    num_elements = len(arr)
    start_elements = [0] * num_elements
    memo = [[-1 for _ in range(num_elements)] for _ in range(num_elements)]

    start_elements[0] = arr[0]
    start_elements[num_elements-1] = arr[num_elements-1]
    if not is_palindrome(start_elements):
        return 0

    print(get_memo(0, num_elements-1, arr, memo))

    return num_elements

