
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # print(n)
    # print(n % 2)
    if n % 2 == 1:
        return False

    nums = []

    for i in range(2, n):
        if i % 2 == 0:
            nums.append(i)

    print(nums)
    s = sum(nums)
    print(s)
    if s == n:
        return True
    else:
        return False

