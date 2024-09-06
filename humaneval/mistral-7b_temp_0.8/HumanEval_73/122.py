
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

    def count_occurrences(arr, char):
        return arr.count(char)

    def make_palindrome(arr):
        if arr == [0]:
            return 0
        if count_occurrences(arr, arr[0]) >= len(arr) // 2:
            return 0
        # count = 0
        # for i in range(len(arr) // 2):
        #     count += abs(arr[i] - arr[len(arr) - 1 - i])
        # return count
        return len(arr) - 2 * count_occurrences(arr, arr[0])

    # count = 0
    # for i in range(len(arr) // 2):
    #     count += abs(arr[i] - arr[len(arr) - 1 - i])
    # return count
    return make_palindrome(arr)

