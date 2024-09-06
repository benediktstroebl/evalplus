
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    if n == 0:
        return -1

    # Set all indices initially as "invalid"
    # Tells us which indices we have tried yet
    # In the case of this problem, it will make us skip some
    # indices later.
    invalid_idx = [True] * n

    # Find the largest value in the array
    largest_value = -1
    largest_idx = -1
    for i in range(n):
        if arr[i] > largest_value:
            largest_value = arr[i]
            largest_idx = i

    # For each element, set the invalid_idx at the largest index
    # Since it is the largest value
    for i in range(n):
        if arr[i] == largest_value:
            invalid_idx[i] = False
            largest_value = -1

    # Now that we have the largest value, we can do a left to right check
    for i in range(n):
        # If the current index is already invalid, skip it
        if invalid_idx[i]:
            continue

        # For this index, find the next largest value
        # Since this is the largest of its value, it must be to the left
        largest_value = -1
        largest_idx = -1
        for j in range(i + 1, n):
            if arr[j] > largest_value:
                largest_value = arr[j]
                largest_idx = j

        # Now find the closest index to this one to the right of it
        # that is not greater than or equal to the largest value
        smallest_value = arr[largest_idx] + 1
        smallest_idx = -1
        for j in range(largest_idx + 1, n):
            if arr[j] < smallest_value:
                smallest_value = arr[j]
                smallest_idx = j

        # Make sure that the smallest value is not greater than or equal to
        # the largest value
        if smallest_value >= largest_value:
            return -1

        # If it is, then set the invalid_idx at the smallest_idx
       
