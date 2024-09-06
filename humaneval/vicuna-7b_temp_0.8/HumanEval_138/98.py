
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    def is_even(x):
        return x % 2 == 0
    def sum_even(x):
        if is_even(x):
            return x
        for i in range(2, x):
            if is_even(x-i):
                if is_even(x-i-1) or is_even(x-i-2):
                    return x
    return sum_even(n) == n
