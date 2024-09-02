
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
    if not arr:
        return 0
    for i in range(1, len(arr)):
        # count the number of elements in the subarray that are less than the center element
        count = 0
        for j in range(i):
            if arr[j] < arr[i]:
                count += 1
        # remove the elements in the subarray in the order of their position
        for k in range(count):
            arr.pop(i)
    # move the remaining elements to the end
    arr.extend(reversed(arr))
    return len(arr) - len(reversed(arr))
