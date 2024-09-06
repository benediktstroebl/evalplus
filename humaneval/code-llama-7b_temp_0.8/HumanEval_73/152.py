
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
    # create a copy of the array
    new_arr = arr[:]
    # reverse the array
    new_arr.reverse()
    # create a new list to keep track of the differences
    diff_list = []
    # iterate through the array
    for i in range(len(arr)):
        # append the difference between the current element and the element in the reversed array to the new list
        diff_list.append(arr[i]-new_arr[i])
    # return the length of the new list
    return len(diff_list)
