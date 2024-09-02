
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
    # validate array input
    if arr is None or len(arr) == 0:
        return 0
    
    # get the half of the array length
    half = len(arr)//2
    
    # create a counter for odd elements
    odd = 0
    
    # create a counter for even elements
    even = 0
    
    # if the length of array is odd
    if len(arr)%2 == 1:
        # count the remaining element in the array
        odd += 1
    
    # iterate from 0 to half
    for i in range(half):
        # if the first and last element is equal
        if arr[i] == arr[-i - 1]:
            # check the next element
            continue
        # if the elements are not equal
        else:
            # if the elements is equal to half length
            if i == half-1:
                # increment the odd
                odd += 1
            # else
            else:
                # increment the even
                even += 1
    
    # if the array is odd length
    if len(arr)%2 == 1:
        # return the odd value
        return odd
    # else
    else:
        # return the min of even and odd value
        return min(even, odd)
    
