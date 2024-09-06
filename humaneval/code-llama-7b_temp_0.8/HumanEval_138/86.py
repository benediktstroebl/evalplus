
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    result = True
    for i in range(2, n-1):
        for j in range(i+1, n//2 + 1):
            for k in range(j+1, (n-i)//2 + 1):
                if (i+j+k) == n and (i+j+k+n) % 2 == 0:
                    return result
                else:
                    continue
    result = False
    return result
