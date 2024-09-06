
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
    # Create a counter variable to track the number of elements that need to be changed
    count = 0
    # Initialize a set to store the numbers that have been seen
    seen = set()
    # Iterate through the array
    for i in range(len(arr)):
        # If the number at index i has been seen, then we can skip it since we can't change it
        if arr[i] in seen:
            continue
        # Otherwise, increment the counter since we need to change the number at index i
        count += 1
        # Add the number at index i to the set of numbers that have been seen
        seen.add(arr[i])
    # Return the counter variable, which represents the minimum number of elements that need to be changed
    return count
