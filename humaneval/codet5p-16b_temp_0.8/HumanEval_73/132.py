
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
    num_changes = 0
    if length % 2 == 0:
        first = arr[:length // 2]
        second = arr[length // 2:]
        for i in range(len(first)):
            if first[i]!= second[len(second) - 1 - i]:
                num_changes += 1
                second[len(second) - 1 - i] = first[i]
    else:
        first = arr[:length // 2]
        second = arr[length // 2 + 1:]
        for i in range(len(first)):
            if first[i]!= second[len(second) - 1 - i]:
                num_changes += 1
                second[len(second) - 1 - i] = first[i]
    return num_changes
