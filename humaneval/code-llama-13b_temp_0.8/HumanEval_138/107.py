
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    x = n/2
    if x - int(x) == 0:
        return False
    x = round(x)
    nums = []
    for i in range(1, x + 1):
        if i % 2 == 1:
            for j in range(1, x + 1):
                if j % 2 == 0:
                    for k in range(1, x + 1):
                        if k % 2 == 1:
                            for q in range(1, x + 1):
                                if q % 2 == 0:
                                    nums.append([i, j, k, q])
    for i in nums:
        if sum(i) == n:
            return True
    return False

