
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

    # Do you know how to find the smallest number of elements that need to be changed to make an array palindromic?
    # Hint: You can change 0 elements in an array that's already a palindrome.
    # Hint: You can't change the first or last elements.
    # Hint: You can't change the first element if it's the same as the last element.

    def is_palindrome(arr):
        if arr == arr[::-1]:
            return True
        else:
            return False

    def num_needed_to_palindrome(arr):
        if is_palindrome(arr):
            return 0
        count = 0
        for i in range(len(arr)):
            if not arr[i] == arr[-i-1]:
                count += 1
        return count

    return num_needed_to_palindrome(arr)

