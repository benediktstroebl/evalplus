
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
    def reverse_array(arr):
        """
        Reverse the array
        """
        return arr[::-1]

    def build_palindrome(arr):
        """
        Build a palindromic array from the given array.
        If the given array is already palindromic, return the same array.
        Otherwise, return an array that is palindromic and consists of elements
        from the given array.
        """
        arr_length = len(arr)
        palindrome = []
        for i in range(arr_length):
            palindrome.append(arr[i])
        # Building palindrome array
        for i in range(arr_length):
            palindrome.append(arr[arr_length - 1 - i])
        return palindrome

    def get_difference_from_palindrome(arr):
        """
        Return the difference between the original array and the palindromic array.
        """
        palindrome = build_palindrome(arr)
        diff = 0
        for i in range(len(
