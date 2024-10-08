
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    result = False
    for i in range(1, int(n/2)+1):
        for j in range(1, int(n/2)+1):
            for k in range(1, int(n/2)+1):
                for l in range(1, int(n/2)+1):
                    if i+j+k+l == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                        result = True
                        return result
    return result

