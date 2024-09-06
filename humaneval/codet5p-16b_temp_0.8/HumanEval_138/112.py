
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    divisors = set()
    for i in range(1,n):
        if n % i == 0:
            divisors.add(i)
    return len(divisors) == 4 and sum([i for i in divisors if i % 2 == 0]) == 4
