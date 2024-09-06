
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    #TODO: Write your solution here
    sum = 0
    if n > 4 and n % 2 == 0:
        for i in range(1, n):
            if i % 2 == 0:
                sum += i
                if sum == n:
                    return True
                elif sum > n:
                    return False
    return False



























