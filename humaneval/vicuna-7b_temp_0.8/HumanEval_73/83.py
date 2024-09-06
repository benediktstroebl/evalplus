
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
    n = len(arr)
    # Sort the array in ascending order
    arr = sorted(arr)

    # Initialize the change variable to the maximum value
    change = max(n - (len(sorted(arr)) // 2), 0)

    # Check if the change variable is less than 1
    if change < 1:
        # Loop through the array
        for i in range(n):
            # Check if the element at index i is smaller than the element to its right
            if arr[i] < arr[i+1]:
                # Swap the element at index i with the element to its right
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # Update the change variable
                change -= 1

    return change