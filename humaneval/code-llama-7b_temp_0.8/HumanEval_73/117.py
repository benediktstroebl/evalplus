
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
    if not arr:
        return 0

    # Set the initial palindrome counter
    count = 1
    total = 0

    for i in range(len(arr)):
        # Find the midpoint
        left, right = arr[:i], arr[i:]
        if left == right:
            continue
        if left == reversed(right):
            # Start from i + 1 to make sure no repeat
            count += 1
            continue
        else:
            # Start from the midpoint to find the smallest change
            for n in range(i, len(arr)):
                left, right = arr[:n], arr[n:]
                if left == reversed(right):
                    break
                total += 1

    return count + total

