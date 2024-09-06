
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    even_numbers = []

    for i in range(n+1):
        if i % 2 == 0:
            even_numbers.append(i)

    for i in range(4):
        for j in range(len(even_numbers)):
            if even_numbers[j] <= n:
                if i == 3:
                    return True
                n -= even_numbers[j]
            if n <= 0:
                break

    return False
