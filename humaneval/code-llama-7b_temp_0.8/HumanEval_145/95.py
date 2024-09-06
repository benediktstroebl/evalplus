
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

    # Solution 1: Brute force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    """
    def sum_digits(n):
        return sum(int(i) for i in str(n))

    return sorted(nums, key=sum_digits)
    """

    # Solution 2: Sorting with the dictionary
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    """
    def sum_digits(n):
        return sum(int(i) for i in str(n))

    nums_dict = {i: sum_digits(i) for i in nums}
    return [num for _, num in sorted(nums_dict.items(), key=lambda x: (x[1], nums.index(x[0])))]
    """

    # Solution 3: Sorting with the custom comparator
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    """
    def sum_digits(n):
        return sum(int(i) for i in str(n))

    def cmp(x, y):
        x_sum = sum_digits(x)
        y_sum = sum_digits(y)
        if x_sum != y_sum:
            return x_sum - y_sum
        return nums.index(x) - nums.index(y)

    return sorted(nums, cmp=cmp)
    """

    # Solution 4: Sorting with the lambda function
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    """
    def sum_digits(n):
        return sum(int(i) for i in str(n))

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))
    """
