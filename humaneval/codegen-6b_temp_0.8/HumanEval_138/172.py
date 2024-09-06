
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_even = 0
    sorted_n = str(n)[::-1]
    for i, x in enumerate(sorted_n):
        if int(x) % 2 == 0:
            sum_even += int(x)
    print(f'sum_even = {sum_even}')
    return sum_even % 2 == 0

