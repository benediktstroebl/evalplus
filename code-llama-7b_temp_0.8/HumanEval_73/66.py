
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
    seen = set()
    res = 0

    # Run through the array and count the number of unique elements
    for elem in arr:
        if elem not in seen:
            seen.add(elem)
        else:
            res += 1

    # Determine the number of unique elements required to make the array palindromic
    # Subtract that number from the number of unique elements in the array
    return len(seen) - res if len(seen) % 2 == 0 else len(seen) - res - 1
