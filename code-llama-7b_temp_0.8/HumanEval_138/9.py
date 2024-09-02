
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_even = 0
    x = n
    for i in range(1,n+1):
        if n%i == 0:
            sum_even = sum_even + i
    return (x%4 == 0 and sum_even%4 == 0 and x//4 == sum_even//4)
