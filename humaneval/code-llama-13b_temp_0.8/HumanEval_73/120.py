
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
    half = len(arr) // 2
    # let's get the half of the array, and make it sorted
    first_half = sorted(arr[:half])
    # if the array has an odd number of elements,
    # we only need to check the left half
    if len(arr) % 2 != 0:
        second_half = arr[half + 1 :][::-1]
    else:
        second_half = arr[half:][::-1]
    changed = 0

    # Let's check both sides, starting from the most left elements
    for i in range(len(first_half)):
        # If the first half and second half are not equal, then let's change them
        if first_half[i] != second_half[i]:
            # and increase the count of changes
            changed += 1
            # We need to decrease the element from the first half,
            # because we will use it to change the second half
            first_half[i] -= 1
            # and increase the element from the second half
            second_half[i] += 1

    return changed

