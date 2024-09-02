
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
    arr.sort()
    # Edge case 0, it is already palindromic
    if (arr == arr[::-1]):
        return 0

    # If we are popping and appending, we can't do anything better than O(n)
    if (arr[0] != arr[-1]):
        return len(arr)

    # We know we have a palindrome, but we need to find the smallest difference
    smallest = len(arr)
    Popped = 0
    # We are going to have to pop until we find a difference of 1 or a palindrome
    while (smallest > 1):
        # We find the smallest difference
        smallest = 1
        for i in range(len(arr)-1):
            if (arr[i] != arr[i+1]):
                smallest = min(smallest, abs(arr[i] - arr[i+1]))

        # We pop the smallest number of times to change the array
        Popped += smallest
        arr.pop()
    return Popped


