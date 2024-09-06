
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
    # the total number of elements
    n = len(arr)
    # the number of elements that are going to be changed
    new_arr = []
    for i in range(n):
        # if the element is even, that means it is already a palindrome, so we don't need to do anything
        if arr[i] % 2 == 0:
            new_arr.append(arr[i])
        else:
            # if the element is odd, we need to change it to a palindrome
            new_arr.append(arr[i] + 1)
    # the number of elements that are going to be changed
    num_of_elements_changed = len(arr) - len(new_arr)
    return num_of_elements_changed
