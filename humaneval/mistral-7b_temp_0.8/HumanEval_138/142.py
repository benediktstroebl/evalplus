
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n % 4 != 0) or (n % 2 != 0):
        return False
    nums = []
    while n > 0:
        if n % 2 == 0:
            nums.append(n)
            n //= 2
        else:
            n //= 2
            nums.append(n)
    return len(nums) == 4




