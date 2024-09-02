
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
    # Write your code here.

    def count_odd_ones(arr):
        count = 0
        for i in arr:
            if i % 2 == 1:
                count += 1
        return count

    def count_even_ones(arr):
        count = 0
        for i in arr:
            if i % 2 == 0:
                count += 1
        return count

    def smallest_change_helper(arr, palindrome):
        """
        This function takes in an array and a palindrome. It then checks if the array is a palindrome and returns
        the number of elements that need to be changed to make the array palindromic. If the array is not a palindrome,
        it returns the number of elements that need to be changed to make the array a palindrome.
        """
        count = 0
        if palindrome:
            count += count_odd_ones(arr)
            return count

        if count_even_ones(arr) == 0:
            return 0

        count
