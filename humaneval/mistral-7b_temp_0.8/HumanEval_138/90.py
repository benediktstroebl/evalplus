
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    def find_factors(n):
        factors = []
        # find factors of n
        i = 1
        while i*i <= n:
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)
            i += 1
        return factors

    factors = find_factors(n)
    if len(factors) != 4:
        return False

    # check if factors can be divided by 2
    factors_divisible = [f for f in factors if f % 2 == 0]
    if len(factors_divisible) != 4:
        return False

    # check if sum of factors is equal to n
    total_sum = sum(factors_divisible)
    return total_sum == n
