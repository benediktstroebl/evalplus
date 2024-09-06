
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

    def count_even_odd(arr):
        """
        returns the number of even numbers and the number of odd numbers in a given array
        """
        odd = 0
        even = 0
        for i in arr:
            if i % 2!= 0:
                odd += 1
            else:
                even += 1
        return even, odd

    def helper(arr, even, odd, index):
        if index > len(arr) - 1:
            return 0

        if index == len(arr) - 1:
            return odd + even - 1

        if count_even_odd(arr[index:]) == (even, odd):
            return helper(arr, even, odd, index + 1)

        if count_even_odd(arr[index:]) == (even, odd + 1):
            return helper(arr, even + 1, odd, index + 1)

        if count_even_odd(arr[index:]) == (even + 1, odd):
            return helper(arr, even, odd + 1, index + 1)

        return helper(arr, even, odd, index +
