
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

    # V1
    # time: O(nlogn)
    # space: O(n)
    # res = sorted(nums, key=lambda x: x, reverse=False)
    # res = sorted(res, key=lambda x: sum(map(int, list(str(x)))), reverse=False)
    # return res

    # V2
    # time: O(nlogn)
    # space: O(n)
    # nums.sort(key = lambda x: sum(map(int, list(str(x)))))
    # nums.sort(key = lambda x: x)
    # return nums

    # V3
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: (sum(map(int, list(str(x)))), -x))

    # V4
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: sum(map(int, list(str(x))))), -x)

    # V5
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: (sum(map(int, list(str(x)))), x))

    # V6
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: sum(map(int, list(str(x)))), x)

    # V7
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: (sum(map(int, list(str(x)))), x), reverse = True)

    # V8
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: sum(map(int, list(str(x)))), reverse = True)

    # V9
    # time: O(nlogn)
    # space: O(n)
    # return sorted(nums, key = lambda x: (sum(map(int, list(str(x)))), x), reverse = True)

    # V10
    # time: O(nlogn)
    # space: O(n)
