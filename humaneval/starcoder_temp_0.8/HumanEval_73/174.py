
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
    length = len(arr)
    if length <= 2:
        return 0

    # count number of odds
    odds = 0
    for n in arr:
        if n % 2 == 1:
            odds += 1

    if odds <= 1:
        return 0

    # set up an array to track count of each number
    # number_counts[n] = number of occurrences of n in arr
    number_counts = [0] * (length + 1)
    for n in arr:
        number_counts[n] += 1

    # set up an array to track count of each number which is a multiple of 2
    # mult_counts[n] = number of occurrences of n in arr which is a multiple of 2
    mult_counts = [0] * (length + 1)
    for n in arr:
        if n % 2 == 0:
            mult_counts[n] += 1

    # set up an array to track count of each number which is a multiple of 2
    # which is not a multiple of 2 and odd
    # odd_counts[n] = number of occurrences of n in arr which is a multiple of 2
    # which is not a multiple of 2 and odd
    odd_counts = [0] * (length + 1)
    for n in arr:
        if n % 2 == 1 and n > 1 and mult_counts[n - 1] > 0:
            odd_counts[n] += 1

    # if n is odd and we can make it even
    # add 1 to the result
    # this is because n will need to be changed to a multiple of 2
    result = 0
    for n in range(3, length + 1):
        if number_counts[n] > 0:
            if mult_counts[n] > 0:
                result += number_counts[n]
            else:
                result += number_counts[n] + odd_counts[n]

    return result

