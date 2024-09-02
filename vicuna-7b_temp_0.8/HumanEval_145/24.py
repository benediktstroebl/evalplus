
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
    def _get_sums(nums):
        sums = [sum(int(n) for n in digits) for digits in nums]
        return sums

    def _sort_by_sums(s):
        index = 0
        result = []
        while index < len(s):
            if s[index] == 0:
                result.append(s[index])
                index += 1
            else:
                num = s[index]
                for i in range(index, len(s)):
                    num += s[i]
                    s[i] = 0
                result.insert(0, num)
                index += 1

        return result

    sums = _get_sums(nums)
    return _sort_by_sums(sums)
