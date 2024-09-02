
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
    # first use the count_array function to count the number of ones in each
    # index.
    # Then use binary_count_array to count the number of ones in each index
    # with binary representation.
    # Then use merge_sort to sort by count_array.
    def sort_lambda(a, b):
        return a < b

    def count_array(arr):
        count = []
        for i in arr:
            count.append(bin(i).count('1'))
        return count

    def binary_count_array(arr):
        count = []
        for i in arr:
            count.append(bin(i).count('1'))
        return count

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        else:
            return arr

    def merge(left, right):
        res = []
        while len(left) > 0 and len(right) > 0:
            if sort_lambda(left[0], right[0]):
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
        if left:
            res += left
        if right:
            res += right
        return res

    return merge(merge_sort(count_array(arr)), binary_count_array(arr))

