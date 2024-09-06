
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
    # Your code goes here
    def is_palindrome(arr):
        """Return True if arr is palindrome, False otherwise"""
        return arr == arr[::-1]

    def count_changes(arr):
        """Return the minimum number of changes to make the array a palindrome"""
        # Check if the array is already a palindrome
        if is_palindrome(arr):
            return 0

        # Check if the array is already reversed
        if arr == arr[::-1]:
            return 0

        # Create a count variable to keep track of the changes
        count = 0

        # Iterate through the array and check if each element is the same as its reverse
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - 1 - i]:
                count += 1

        # Return the minimum number of changes to make the array a palindrome
        return count

    return count_changes(arr)

