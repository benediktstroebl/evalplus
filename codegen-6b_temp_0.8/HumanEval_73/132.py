
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
    """
    initialize three pointers `start`, `mid` and `end` initially to the left and right of given array respectively
    
    while start <= end:
        increment to the middle
        
        if arr[mid] is less than the middle element:
            increment start
        else if arr[mid] is greater than the middle element:
            decrement end
        else:
        
            if start <= end:
                if arr[start] > arr[end]:
                    arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                
    return 0
    
    """
    if not arr:
        return 0
    start, end = 0, len(arr) - 1
    while start <= end:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        mid = (start + end) // 2
        if arr[mid] < arr[end]:
            start = mid + 1
        elif arr[mid] > arr[end]:
            end = mid - 1
        else:
            if (end - start) < (end - mid):
                end = mid
            else:
                start = mid + 1
    return start - end
