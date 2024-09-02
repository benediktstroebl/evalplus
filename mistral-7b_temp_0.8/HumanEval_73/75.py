
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
    # Create a dictionary to store the element counts
    counts = {}

    # Count the occurrences of each element in the array
    for element in arr:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1

    # Find the minimum number of changes needed to make the array palindromic
    min_changes = 0
    for element, count in counts.items():
        if count % 2 == 1:
            min_changes += 1

    return min_changes
