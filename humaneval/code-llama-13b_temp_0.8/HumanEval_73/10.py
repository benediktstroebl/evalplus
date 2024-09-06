
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

    num_changes = 0
    palindrome = [x for x in arr]
    mid_index = len(arr) // 2
    if len(arr) % 2 != 0:
        mid_index += 1

    for i in range(mid_index):
        left = i
        right = len(arr) - 1 - i

        if palindrome[left] != palindrome[right]:
            num_changes += 1
            while left < right and palindrome[left] != palindrome[right]:
                palindrome[right] = palindrome[left]
                left += 1
                right -= 1

    return num_changes
