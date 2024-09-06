def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Create a reversed copy of the array
    rev = arr[:]
    rev.reverse()
    # Calculate the number of common elements between the array and its reverse
    return len(arr) - len(set(arr).intersection(set(rev)))