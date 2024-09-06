
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
    # Check if the array is empty
    if not arr:
        return 0

    # Find the first and last elements of the array
    first = arr[0]
    last = arr[-1]

    # Count the number of elements in the array
    n = len(arr)

    # Initialize variables to track the minimum number of changes and the first element
    min_changes = n + 1
    min_change = first

    # Loop through the array
    for i in range(1, n):
        # Find the next and previous elements
        next = arr[i]
        prev = first

        # Check if the current element is the first or last
        if i == 0 or i == n - 1:
            # If the current element is the first or last, we don't need to make any changes
            if arr[i] == next:
                continue

        # Check if the current element is adjacent to the previous element
        if next not in (first, last):
            # If the current element is not adjacent to the previous element, we need to make 1 change
            min_changes -= 1

        # Update the minimum number of changes and the first element
        min_changes -= 1
        min_change = next

    return min_changes