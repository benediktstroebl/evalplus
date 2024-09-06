
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
    if len(arr) == 0:
        return 0

    list_of_changes = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] or arr[i] + arr[j] == arr[j] + arr[i]:
                continue
            else:
                list_of_changes.append([arr[i], arr[j]])
    print(list_of_changes)
    # count = 0
    # while len(list_of_changes) > 0:
    #     count += 1
    #     for pair in list_of_changes:
    #         if pair[0] < pair[1]:
    #             list_of_changes.remove(pair)
    #             break
    #         else:
    #             list_of_changes.remove(pair)
    # print(count)
    return len(list_of_changes)
