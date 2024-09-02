
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    ans = False
    # do not forget to store your answer here
    for i in range(2, int(n ** 0.5)):
        if n - i * i == i:
            if n / i % 2 == 0:
                if int(n / i) == i:
                    ans = True
            else:
                ans = True
    return ans
