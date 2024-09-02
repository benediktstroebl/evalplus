
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
    # Find the indexes of the middle
    mid_index = len(arr)//2
    num_left = arr[:mid_index]
    num_right = arr[mid_index:]

    # Check if the left and right side are palindromes
    is_left_palindrome = is_right_palindrome = True

    # If there is an odd number of elements, reverse the first half to check if it is palindromic
    if len(num_left) % 2 != 0:
        num_left = num_left[::-1]

    # Check if the left side is a palindrome
    for i in range(len(num_left) // 2):
        if num_left[i] != num_left[-i - 1]:
            is_left_palindrome = False
            break

    # Check if the right side is a palindrome
    for i in range(len(num_right) // 2):
        if num_right[i] != num_right[-i - 1]:
            is_right
