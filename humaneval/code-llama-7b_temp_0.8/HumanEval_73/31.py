
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
    n = len(arr)
    if n == 0 or n == 1:
        return 0

    # preprocessing
    hash = {}
    for i in range(n):
        if arr[i] not in hash:
            hash[arr[i]] = [i]
        else:
            hash[arr[i]].append(i)

    odd_count = 0
    even_count = 0
    for i in hash:
        if len(hash[i]) % 2 == 1:
            odd_count += 1
        else:
            even_count += 1

    # print(hash)
    if odd_count == 0:
        return 0
    elif odd_count % 2 == 0:
        return int(even_count / 2)
    else:
        return int((even_count / 2) + 1)

