
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    sum_even_numbers = 0
    while True:
        #print(sum_even_numbers)
        if n < sum_even_numbers:
            return False
        else:
            if n == sum_even_numbers:
                return True
            else:
                n = n - 2
                sum_even_numbers = sum_even_numbers + 2


