
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

    # O(n) time and space
    hashmap = {num: index for index, num in enumerate(arr)}

    # find the value of the middle element
    mid = len(arr) // 2
    # get the index of the middle element
    middle = hashmap[arr[mid]]

    smallest_pal = []
    for index, num in enumerate(arr):
        if num != arr[middle]:
            smallest_pal.append((num, arr[middle], index, middle))

    smallest_pal.sort(key=lambda x: (abs(x[0] - x[1]), x[2], x[3]))
    return len(smallest_pal)

