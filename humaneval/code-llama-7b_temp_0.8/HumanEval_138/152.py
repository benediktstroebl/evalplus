
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Remark:
    # the function is_even takes two parameters, which are not really needed here

    sum = 0
    # here, we need to write 4 "for" loops.
    # Hint: you can reuse the variables "sum" and "n"
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                for d in range(1, n+1):
                    sum = a + b + c + d
                    if sum == n:
                        return True
    return False

