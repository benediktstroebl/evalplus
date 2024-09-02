
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False

    for i in range(1,n):
        for j in range(1,n):
            if i == j:
                continue
            for k in range(1, n):
                for m in range(1,n):
                    if i == k or i == m or j == k or j == m:
                        continue
                    if n == i + j + k + m and n%2 == 0:
                        return True
    return False
    
