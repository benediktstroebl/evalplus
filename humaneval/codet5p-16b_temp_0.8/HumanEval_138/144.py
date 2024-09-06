
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = str(n)
    evens = []
    for num in n:
        if int(num) % 2 == 0:
            evens.append(int(num))
    summ = sum(evens)
    if int(n) == summ:
        return True
    return False

