
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

    # Find the median in O(n)
    # The first half of the array is greater than the median, the second half is less than the median
    # Count the number of swaps needed for each half
    # If the median is odd, can just divide by 2
    # If the median is even, can divide by two and add one if the second half is longer
    #
    # O(n)
    #
    def median(arr):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[hi]:
                hi = mid
            elif arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = hi - 1
        return arr[hi]

    arr = sorted(arr)
    mid = median(arr)
    lo, hi = 0, len(arr) - 1
    l_diff, r_diff = 0, 0
    while lo < hi:
        if arr[lo] < mid:
            l_diff += 1
        elif arr[hi] > mid:
            r_diff += 1
        lo += 1
        hi -= 1
    return min(l_diff, r_diff)
