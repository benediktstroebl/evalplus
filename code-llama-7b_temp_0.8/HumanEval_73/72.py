
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
    # A palindrome is a string that is read the same backwards and forwards
    # We need to see how many elements are different from their counterpart
    # in the reverse of the array
    # Start with an array of 0s for tracking each index
    # Iterate through each element and track the number of instances
    # where the element is not equal to the element in the reversed array
    # at the same index
    # Return the sum of these instances
    count = [0] * len(arr)
    # Get the reversed array
    reverse = arr[::-1]
    # Iterate through the arr to compare with the reversed array
    for i in range(len(arr)):
        # If they do not match, add 1 to the index counter
        if arr[i] != reverse[i]:
            count[i] = 1
    return sum(count)

