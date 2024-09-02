
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 2:
        return True
    if n % 2!= 0:
        return False

    nums = set([x for x in range(1, n // 2 + 1)])

    for i in range(3, n, 2):
        if i in nums and i % 2 == 0:
            nums.remove(i)
    return n == sum(nums)
