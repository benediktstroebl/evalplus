
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_list = [int(i) for i in str(n)]
    n_list = [i for i in n_list if i%2==0]
    sum_even = 0
    for i in n_list:
        sum_even += i
    return sum_even == n
