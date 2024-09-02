
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
    # Need to start at the middle of the array to figure out if it's a palindrome
    # or not.
    # Also need to figure out if it's a multiple of 2 or not.
    # If it's even, then you just need to see if the two middle sections are equal.
    # If it's odd, then you need to see if the first and last elements are equal.
    # If that's true, then you need to see if the middle element is equal to any of
    # the elements in the middle.
    # If any of the elements in the middle are equal to the middle element, then you
    # only need to change one of them to make the array palindromic.
    # Otherwise, you need to change two elements to make it palindromic.

    def is_palindrome(arr):
        # Check to see if the first half of the array is equal to the second
        # half of the array.
        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True

    def find_palindrome_change(arr):
        # You can't change the first or last element
        changes = 1
        # Look through the middle half of the array
        for i in range(len(arr) // 2):
            # If there are equal elements in the middle, then you're done
            if arr[i] == arr[len(arr) - 1 - i]:
                return changes
            else:
                changes += 1
        return changes

    def find_odd_palindrome_change(arr):
        # Need to check the middle element against the first and last elements
        changes = 2
        # If the middle element is the same as the first or last element, then
        # we're done
        if arr[len(arr) // 2] == arr[0] or arr[len(arr) // 2] == arr[len(arr) - 1]:
            return changes
        # Loop through the array
        for i in range(len(arr) - 1):
            # If the middle element is the
