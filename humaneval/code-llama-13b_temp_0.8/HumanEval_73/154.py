
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
    odd_count = 0
    # since we need to use dictionary for our solution we are using the built in one
    result = {}
    # loop over the array to count how many odd numbers are there
    for i in range(len(arr)):
        # first check if the number is odd
        if arr[i] % 2 != 0:
            odd_count += 1
        # then check if the number is already in the dictionary
        if arr[i] in result:
            # if so increment it by 1
            result[arr[i]] += 1
        else:
            # else add it to the dictionary
            result[arr[i]] = 1
    # if there are no odd numbers, the minimum required changes is 0
    if odd_count == 0:
        return 0
    # if the length of the dictionary is 1 and the count of the only item is odd, then also the minimum required changes is 0
    elif odd_count % 2 != 0 and len(result) == 1:
        return 0
    # else return half of the total changes required
    else:
        return int(sum(result.values()) / 2)
