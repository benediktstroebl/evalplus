
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

    # time to do this is O(n)

    # change the array to be a list of counts of each element
    # let's call this arr_counts
    arr_counts = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        arr_counts[arr[i] - 1] += 1

    # make sure that if the array is already palindromic, we don't try to change any
    if (arr[0] == arr[len(arr) - 1]):
        return 0

    # keep track of our result
    result = len(arr) - 1

    # each of our three possible changes requires an array of counts that is
    # a little different. These arrays are called arr_odd, arr_even, and arr_middle.
    # these arrays are used so that we can keep track of how many times we can
    # change each element, without having to recount every element.

    # the way these arrays are filled in is:
    # for each of the three cases,
