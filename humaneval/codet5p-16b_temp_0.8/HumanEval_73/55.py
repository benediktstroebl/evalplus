
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

    def is_palindromic(array):
        return all(array[i] == array[len(array) - 1 - i] for i in range(len(array) // 2))
    changes = 0
    while not is_palindromic(arr):
        most_common_item = max(arr, key=arr.count)
        most_common_item_count = arr.count(most_common_item)
        changes += most_common_item_count - 1
        arr = [item for item in arr if item!= most_common_item]
    return changes

