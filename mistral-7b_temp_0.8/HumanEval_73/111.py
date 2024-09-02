
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
    # Change array to string.
    arr = ''.join([str(i) for i in arr])

    # Use zip to create array of matching elements.
    arr = zip(arr, arr[::-1])

    # Create array of mismatched elements.
    arr = [i[0] for i in arr if i[0] != i[1]]

    # Remove duplicates.
    arr = set(arr)

    # Return length of list.
    return len(arr)

