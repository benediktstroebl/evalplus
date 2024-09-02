
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_evens = []
    for i in range(2, n):
        if n % i == 0:
            sum_evens.append(i)

    sum_evens = list(filter(lambda x: x % 2 == 0, sum_evens))
    if len(sum_evens) == 4:
        return sum(sum_evens) == n
    else:
        return False

