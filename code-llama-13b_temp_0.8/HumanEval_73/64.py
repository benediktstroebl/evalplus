
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
    mid_index = length // 2
    # Get the length of the longest palindrome from the middle outwards
    max_palindrome_length = 0
    for i in range(mid_index + 1):
        left = i
        right = length - 1 - i
        if arr[left] != arr[right]:
            max_palindrome_length = max(i, right - left)
        else:
            while left > 0 and right < length - 1:
                if arr[left - 1] == arr[right + 1]:
                    left -= 1
                    right += 1
                else:
                    break
            max_palindrome_length = max(max_palindrome_length, right - left + 1)
    return length - 2 * max_palindrome_length + 1

