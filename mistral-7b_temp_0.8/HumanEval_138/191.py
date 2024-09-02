
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    #TODO: write your implementation here
    if n == 8:
        return True
    elif n < 8:
        return False
    else:
        l = []
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(2, n):
            for j in range(2, n):
                for k in range(2, n):
                    for l in range(2, n):
                        a = i + j
                        b = j + k
                        c = k + l
                        d = l + n
                        if a + b + c + d == n:
                            return True
        return False
