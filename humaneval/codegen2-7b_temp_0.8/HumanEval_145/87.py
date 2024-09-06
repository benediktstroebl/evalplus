
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
    
    def get_sum(num):
        """
        Return sum of digits of a given number.
        """
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    
    return sorted(nums, key=lambda x: get_sum(x), reverse=
