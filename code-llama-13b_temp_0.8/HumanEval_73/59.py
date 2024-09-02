
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

    def is_palindrome(num_list):
        return num_list == num_list[::-1]

    # Initialize number of changes as 0
    changes = 0

    # Get the length of list
    n = len(arr)

    # Create two pointers, one from beginning of array and one from end of array
    front_index = 0
    back_index = n - 1

    # One by one compare elements at both ends
    while front_index < back_index:
        # If elements do not match, then increment sum and move both pointers one step forward
        if arr[front_index] != arr[back_index]:
            changes += 1
            front_index += 1
            back_index -= 1
        # If elements match
        else:
            # Move both pointers one step towards each other
            front_index += 1
            back_index -= 1
    # If palindrome is not possible, return -1
    if changes > 0:
        return changes
    # Find the first occurrence of mismatch from both ends
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return 2
    return 0

