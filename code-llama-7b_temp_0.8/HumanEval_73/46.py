
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

    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == arr[right]:
            left += 1
            right -= 1
        if left >= right:
            break

        # Set the left and right pointers to the first different elements
        left_pivot = arr[left]
        right_pivot = arr[right]

        # If the left and right pivots are the same, advance one or the other
        if left_pivot == right_pivot:
            left += 1
            right -= 1

        # If the left and right pivots are different, find the smallest swap
        else:
            pivot = find_minimum_swap(left_pivot, right_pivot, arr)

            # Adjust the count based on the smallest swap
            return pivot - 1

    # Return the number of swaps that result in a palindrome
    return 0

