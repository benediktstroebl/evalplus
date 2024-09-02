
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    def _sort_array(left, right, nums):
        if left > right:
            return None

        if (left + right) % 2 == 0:
            mid = (left + right) // 2
            left_num, right_num = _sort_array(left, mid, nums), _sort_array(mid + 1, right, nums)
            left_sums, right_sums = sum(left_num), sum(right_num)
            if left_sums < right_sums:
                return left_num + [nums[mid]] + right_num
            elif left_sums > right_sums:
                return left_num + right_num + [nums[mid]]
            else:
                left_sums, right_sums = sum(left_num), sum(right_num)
                i, j = 0, 0
                while i < left_sums and j < right_sums:
                    if left_num[i] < right_num[j]:
                        return left_num[:(i + 1)] + [nums[mid]] + right_num[i:]
                    elif left_num[i] > right_num[j]:
                        return left_num[i:] + [nums[mid]] + right_num[:(j + 1)]
                    else:
                        i += 1
                        j += 1
                if left_num < right_num:
                    return left_num + [nums[mid]] + right_num[j:]
                else:
                    return left_num + right_num + [nums[mid]]
        else:
            mid = (left + right) // 2
            left_num, right_num = _sort_array(left, mid, nums), _sort_array(mid + 1, right, nums)
            left_sums, right_sums = sum(left_num), sum(right_num)
            if left_sums < right_sums:
                return left_num + right_num + [nums[mid]]
            else:
                left_sums, right_sums = sum(left_num), sum(right_num)
                i,