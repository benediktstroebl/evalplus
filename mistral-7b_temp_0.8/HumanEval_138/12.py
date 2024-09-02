
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    counter = 0
    total = 0
    if n % 2 == 0:
        for i in range(n + 1):
            if i % 2 == 0:
                counter += 1
                total += i
            if counter == 4:
                break
        if total == n:
            return True
        else:
            return False
    else:
        return False
