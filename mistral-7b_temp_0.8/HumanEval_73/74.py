
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

    # print(len(arr))

    hash_map = dict()
    for i in range(len(arr)):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 1
        else:
            hash_map[arr[i]] += 1

    #print(hash_map)

    arr_str = ''.join(map(str, arr))
    #print(arr_str)

    arr_str_reversed = arr_str[::-1]
    #print(arr_str_reversed)

    count = 0

    for i in range(len(arr_str)):
        if arr_str[i] != arr_str_reversed[i]:
            count += abs(hash_map[arr_str[i]] - hash_map[arr_str_reversed[i]])
            #print(arr_str[i], arr_str_reversed[i])

    return count

