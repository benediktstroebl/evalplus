
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
    # Add a guard to make sure arr is not empty
    if len(arr) == 0:
        return 0

    # If there's only 1 item in the array, we're done
    if len(arr) == 1:
        return 0

    odd_count = 0
    even_count = 0

    # Count the number of odds and evens
    for item in arr:
        if item % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # If there's an odd number of elements, we can't do it
    if odd_count % 2 != 0:
        return -1

    # If there's an even number of evens, we're done
    if even_count % 2 == 0:
        return 0

    # If there's an odd number of odds, we can get rid of the minimum odd
    if odd_count % 2 != 0:
        return 1

    # If we get to here, it's an even number of odds and evens
    return 0
