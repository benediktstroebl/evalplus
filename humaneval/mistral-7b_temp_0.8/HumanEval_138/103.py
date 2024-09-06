
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    def check_even(x):
        return x % 2 == 0
    def check_positive(x):
        return x >= 0
    def is_sum_of_even_numbers(num):
        for i in range(1, int(num / 2)):
            if (num - 2 * i) % 4 == 0:
                if check_even(num - 2 * i) and check_positive(num - 2 * i):
                    return True
        return False
    return is_sum_of_even_numbers(n)

