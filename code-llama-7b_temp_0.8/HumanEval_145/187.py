
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
    def sort(nums):
        nonlocal digits_sums
        if not nums:
            return

        for i in range(len(nums)):
            num = nums[i]
            digits_sum = sum(int(i) for i in str(num))
            if digits_sum not in digits_sums:
                digits_sums[digits_sum] = i

            next_index = digits_sums[digits_sum]
            while nums[next_index] and digits_sums[sum(int(i) for i in str(nums[next_index]))] < next_index:
                next_index = digits_sums[sum(int(i) for i in str(nums[next_index]))]
            nums[i], nums[next_index] = nums[next_index], nums[i]

        for i in range(len(nums)):
            nums[i] = nums[i] if nums[i] != 0 else nums.pop()

        next_index = digits_sums[digits_sums[nums[0]]]
        nums[0], nums[next_index] = nums[next_index], nums[0]
        sort(nums[:next_index])
        sort(nums[next_index+1:])

    digits_sums = {}
    sort(nums)
    return nums

