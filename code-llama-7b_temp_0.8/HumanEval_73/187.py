
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

    # Start with the largest palindrome possible
    max_palindrome_size = len(arr) // 2
    for palindrome_size in reversed(range(1, max_palindrome_size+1)):
        # Compare the left and right part of the palindrome
        left_index = palindrome_size-1
        right_index = len(arr)-palindrome_size
        while (left_index >= 0) and (right_index < len(arr)) and (arr[left_index] == arr[right_index]):
            left_index -= 1
            right_index += 1
        if left_index < 0 or right_index >= len(arr):
            return 0

    # We found the first palindrome index
    # Find the number of differences between the two sides
    differences = []
    left_index = palindrome_size-1
    right_index = len(arr)-palindrome_size
    while (left_index >= 0) and (right_index < len(arr)):
        differences.append(abs(arr[left_index]-arr[right_index]))
        left_index -= 1
        right_index += 1

    return max(differences)

