
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

    # This is a one pass method
    # I think this is the fastest for the case that the array has one reversed sequence
    # O(n) time complexity

    reverse_index = len(arr) - 1
    reversed_arr = arr[::-1]
    count = 0

    # Check to see if the array is already palindromic
    for i in range(len(arr)):
        if arr[i] != reversed_arr[i]:
            # If not then the array is not palindromic
            count += 1

            # If there is an odd number of elements, then we need to find the midpoint of the palindromic half and swap it with the mirror element
            if count % 2 != 0:
                arr[reverse_index] = arr[reverse_index] - 1
                arr[i] = arr[reverse_index]

            # If there is an even number of elements, then we can swap the midpoints of the palindromic halves
            else:
                arr[reverse_index] = arr[
