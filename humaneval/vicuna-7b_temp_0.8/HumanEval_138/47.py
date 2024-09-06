
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 == 0:
        return False
    # Check if n can be represented as the sum of 4 numbers
    nums = list(range(1, n + 1))
    if len(nums) != 4:
        return False
    # Check if the remaining numbers can be summed to be even
    if sum(nums[1:]) % 2 != 0:
        return False
    if sum(nums[1:]) % 4 != 0:
        return False
    return True
