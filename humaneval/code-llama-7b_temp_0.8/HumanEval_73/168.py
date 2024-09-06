
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
    len_arr = len(arr)
    # If array is empty or the elements are already a palindrome, return 0
    if len_arr <= 1 or all([arr[i] == arr[len_arr - 1 - i] for i in range(len_arr // 2)]):
        return 0

    # If the array is palindrome in odd length,
    # just return the index of the element that is not equal to its reverse
    if len_arr % 2 == 1:
        return 1

    # If the array is palindrome in even length,
    # return the minimum of the following:
    # 1) the index of the element that is not equal to its reverse
    # 2) the number of elements that are not equal to their corresponding reversed element
    for i in range(len_arr // 2):
        if arr[i] != arr[len_arr - 1 - i]:
            return 1
    return 2
