
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
    # first, find the first non-duplicate character
    left, right = 0, len(arr) - 1
    while left < right and arr[left] == arr[right]:
        left += 1
        right -= 1
    # check if array is already palindromic
    if left >= right:
        return 0
    # for a palindrome, we need to have half of them as the left side
    # and half as the right side
    # so, we can now count the left side characters
    count = collections.Counter(arr[:right + 1])
    # now we need to find the smallest number of right side characters
    # to make the left side equal to the right side
    # let's start by making a dictionary of the left side counts
    # and their left sides
    need = {}
    for k, v in count.items():
        if v % 2 == 1:
            need[k] = v
    # now we need to find the right side counts
    # but this time, we can skip duplicates
    right_count = collections.Counter(arr[right + 1:])
    right_side = []
    for k, v in right_count.items():
        if k in need:
            if v > need[k]:
                right_side.append((k, v - need[k]))
    # the right side is sorted in decreasing order
    # so, we just need the sum of the first half
    return sum(i[1] for i in right_side[:len(right_side) // 2])

