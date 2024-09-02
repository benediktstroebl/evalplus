
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
    # arr = [1,2,3,5,4,7,9,6]
    # arr = [1, 2, 3, 4, 3, 2, 2]
    # arr = [1, 2, 3, 2, 1]
    # arr = [1,2,3,4,5,6,7,8,9,1,2,3]
    # arr = [1,2,3,4,5,6,7,8,9,1,2,3,4]
    # arr = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1]
    # arr = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2, 3]
    # arr = [1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2, 3, 4]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # # reverse array
    # rev_arr = arr[::-1]

    # # add the arrays
    # sums = [x + y for (x, y) in zip(arr, rev_arr)]
    # sums = [x - y for (x, y) in zip(sums, arr)]

    # # create a set of values
    # vals = set(sums)

    # # find the number of occurances of each element in the sums
    # counts = {}
    # for val in vals:
    #     counts[val] = sums.count(val)

    # # find the smallest value
    # smallest = min(counts)

    # # return the number of changes required to make the smallest element 0
    # return smallest - counts[smallest]

    # create a hash to store values
