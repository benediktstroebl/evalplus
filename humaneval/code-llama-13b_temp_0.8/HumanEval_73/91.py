
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

    # To be a palindrome, the first half must be equal to the reverse of the second half
    # We don't actually need to find the reverse, just make sure we have the same number
    # of occurances of each half

    # If we can find the first half and second half, we just need to find the differences
    # between the numbers in the first half and second half

    if len(arr) < 2:
        return 0

    left_half = 0
    right_half = len(arr) - 1

    first_half = {}
    second_half = {}
    count = 0

    while left_half < right_half:
        while arr[left_half] == arr[right_half]:
            left_half += 1
            right_half -= 1
            if left_half >= right_half:
                break
        if arr[left_half] in first_half:
            first_half[arr[left_half]] += 1
        else:
            first_half[arr[left_half]] = 1
        if arr[right_half] in second_half:
            second_half[arr[right_half]] += 1
        else:
            second_half[arr[right_half]] = 1
        left_half += 1
        right_half -= 1

    for key in first_half:
        if key not in second_half:
            second_half[key] = 0
        if first_half[key] != second_half[key]:
            count += abs(first_half[key] - second_half[key])
        else:
            count += 0

    return count

