
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = []
    for i in range(1, n):
        for j in range(1, n):
            if i + j == n and i % 2 == 0 and j % 2 == 0:
                numbers.append(i)
                numbers.append(j)

    if len(numbers) == 4:
        return True
    return False
