
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = list(range(2, (n // 2) + 1))
    odds = []

    while numbers:
        if n % numbers[0] == 0:
            n = int(n / numbers[0])
            odds.append(numbers[0])
        else:
            numbers.pop(0)

    if len(odds) == 4:
        return True
    else:
        return False

