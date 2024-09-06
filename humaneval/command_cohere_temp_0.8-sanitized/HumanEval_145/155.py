def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers with no guaranteed order.

    Returns:
        list: Ordered list according to criteria above.
    """
    if not nums:
        return []

    # Counter for tracking the sum of digits for each number
    digit_sum_count = [0] * 10

    # List to store the sorted numbers
    sorted_nums = []

    # Helper function to extract the sum of digits of a number
    def get_digit_sum(num):
        nonlocal digit_sum_count
        sum_of_digits = 0
        while num > 0:
            digit_sum_count[num % 10] += 1
            sum_of_digits += (num % 10)
            num //= 10
        return sum_of_digits

    # Sorting and building the final list
    for n in nums:
        digit_sum = get_digit_sum(n)
        original_index = nums.index(n) if n in nums else len(nums)
        sorted_nums.append(
            n
            if digit_sum_count[digit_sum] == 1
            else sorted_nums[digit_sum_count[digit_sum] - 1]
            if original_index
            != len(nums) - 1
            and sorted_nums[digit_sum_count[digit_sum] - 1] != n
            and digit_sum_count[digit_sum] > 0
            else n
        )
        digit_sum_count[digit_sum] -= 1

    return sorted_nums