
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
    # Sort the array
    arr = sorted(arr)
    
    # Initialize variables to keep track of the number of elements in the array
    # and the number of elements that need to be changed to make the array palindromic
    n = len(arr)
    min_change = n
    # Check if the array is already palindromic
    if arr == sorted(arr):
        return 0
    # Check if the array is a palindrome
    for i in range(n-1):
        if arr[i] != arr[n-i-1]:
            return n
    # Check if the array has more than one element
    if n == 1:
        return 1
    
    # Iterate through the array
    for i in range(n-1):
        # Try to make the array palindromic by changing one element
        for j in range(n-i-1):
            arr[i], arr[j] = arr[j], arr[i]
            if sorted(arr) != arr:
                break
        else:
            # If no element can be changed to make the array palindromic,
            # then the minimum number of elements that need to be changed
            # is i+1
            min_change = min(min_change, i+1)
    return min_change