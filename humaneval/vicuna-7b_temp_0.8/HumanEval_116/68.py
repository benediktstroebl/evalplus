
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def binary_search(arr, target):
        """
        Binary search algorithm to find the index of the target in the arr.
        """
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def count_leading_ones(num):
        """
        Count the number of leading ones in the binary representation of a number.
        """
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num //= 2
        return count

    def compare(num1, num2):
        """
        Compare two numbers based on their binary representation, then on their
        decimal value.
        """
        num1_count = count_leading_ones(num1)
        num2_count = count_leading_ones(num2)
        if num1_count == num2_count:
            return cmp(num1, num2)
        else:
            return cmp(num1_count, num2_count)

    arr = sorted(arr, key=compare)
    return arr