
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
    max_count = 0
    for i in range(len(arr)):
        # print(f'{arr[i-1]}, {arr[i]}')
        count = 0
        for j in range(i, len(arr)):
            if arr[i-1] == arr[j]:
                count += 1
            else:
                break
        for j in range(i-1, -1, -1):
            if arr[i-1] == arr[j]:
                count += 1
            else:
                break
        max_count = max(max_count, count)
    return max_count
