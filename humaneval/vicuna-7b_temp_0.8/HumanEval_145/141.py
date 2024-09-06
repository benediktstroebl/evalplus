
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def get_digit_sum(num):
        """
        Returns the sum of digits of the given number
        """
        return sum(int(n) for n in str(num))

    def get_index(num):
        """
        Returns the index of the given number in the list
        """
        return num - num // int(num // 10)

    def apply_sort(lst, digits):
        """
        Applies the sorting on the given list and returns the sorted list
        """
        lst.sort(key=lambda x: (get_digit_sum(x), get_index(x)))
        return lst

    sorted_lst = apply_sort(nums, get_digit_sum)
    return sorted_lst
