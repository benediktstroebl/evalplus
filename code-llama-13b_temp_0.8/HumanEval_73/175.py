
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
    if len(arr) < 2:
        return 0

    # We will use a memo table to store partial results
    # Each entry is keyed by the start and end of a subarray
    # Each entry is the minimum number of changes to make a subarray palindromic
    memo = {}

    def min_changes(start, end):
        # Base case: an array of length 1
        if start == end - 1:
            return 0

        # Check the memo table for a cached result
        if (start, end) in memo:
            return memo[(start, end)]

        # Our goal is to make an array palindromic. We will recursively find the
        # smallest number of changes by trying to split the array in two and
        # find the minimum number of changes in each half, then taking the
        # minimum of the two.

        # To split the array in two, we first calculate the number of changes
        # needed for the left half.
        left = min_changes(start, (start + end) // 2)

        # Next, calculate the number of changes needed for the right half.
        right = min_changes((start + end) // 2, end)

        # Now find the minimum of the two
        min_changes_so_far = min(left, right)

        # We now have the number of changes needed to make a subarray palindromic.
        # The original question was to find the minimum number of changes needed
        # to make the entire array palindromic, so now we find how many changes
        # we can make by fixing the left half and right half.

        # Get the left and right halves
        left_half = arr[start : (start + end) // 2]
        right_half = arr[(start + end) // 2 : end]

        # Count the number of changes in the left half
        left_changes = 0
        left_pointer = 0
        right_pointer = 0
        while left_pointer < len(left_half) and right_pointer < len(right_half):
            if left_half[left_pointer] != right_
