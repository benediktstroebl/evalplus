
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
    # First, let's count the occurrences of each number. We can use a dictionary, for
    # example:
    # count = {1: 3, 2: 2, 3: 1, 4: 3}
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # Now, we need to find the half of the length of the array, rounded up. For
    # example:
    # half_length = 5
    half_length = len(arr) // 2 + len(arr) % 2
    # Now, we need to find the half of the length of the array, rounded up. For
    # example:
    # odd = True
    odd = len(arr) % 2 == 1
    # Find the sum of the occurrences of each number that occurs more than or equal
    # to the half of the length of the array. For example:
    # sum_half = 13
    sum_half = 0
    for i in count:
        if count[i] >= half_length:
            sum_half += count[i]
    # Now, the answer is the sum of the occurrences minus the number of elements
    # that occur more than the half of the length of the array, plus the number of
    # elements that are odd:
    # return sum(count.values()) - sum_half + odd
    return sum(count.values()) - sum_half + odd
