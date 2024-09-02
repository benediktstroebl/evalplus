
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

    # make a set from the array
    set_arr = set(arr)
    # create a dictionary that maps the number of occurences of each integer
    # to that number itself
    counts = {i: arr.count(i) for i in set_arr}
    # filter out the numbers with only 1 occurence
    # get the sum of the number of occurences of each number and divide by 2
    return sum(1 for x in counts.values() if x % 2 == 1) // 2
