
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2 == 1:
        return False
    else:
        sum = 0
        count = 1
        while sum < n:
            sum += count
            count += 2
            if sum == n:
                return True
        return False

