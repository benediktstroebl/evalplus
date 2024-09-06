
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = []
    for i in range(1, n//2 + 1):
        if (n - 2*i) % (2*i) == 0:
            numbers.append(i)
            numbers.append(n - 2*i)
            break
    return len(numbers) == 4

