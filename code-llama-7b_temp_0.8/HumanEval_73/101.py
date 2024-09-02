
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

    # palindrome is the maximum palindrome that could start from arr[0]
    palindrome = 0
    for i in range(1, len(arr)):
        # if current number is smaller than arr[0] it doesn't help us
        # to get palindrome of arr.
        if arr[i] <= arr[palindrome]:
            continue

        # If not palindrome, check if can grow palindrome from arr[i]
        left_bound = palindrome * 2 + 1
        right_bound = i
        while left_bound <= right_bound:
            middle = (left_bound + right_bound) // 2
            if arr[middle] >= arr[i]:
                left_bound = middle + 1
            else:
                right_bound = middle - 1

        palindrome = left_bound

    return len(arr) - palindrome
