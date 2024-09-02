
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
    # sort the array
    arr = sorted(arr)
    
    # initialize the minimum number of changes to the length of the array
    min_changes = len(arr)
    
    # initialize the end index
    end_index = 0
    
    while end_index < len(arr) - 1:
        # check if the subarray from the start to the end index is a palindrome
        if arr[start_index:end_index] == arr[end_index:start_index]:
            # update the minimum number of changes and the start index
            min_changes = min(min_changes, end_index - start_index + 1)
            start_index += 1
        end_index += 1
    
    # return the minimum number of changes
    return min_changes