
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # We will store the even numbers in a list
    even_numbers = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    if len(even_numbers) < 4:
        return False
    else:
        print(even_numbers)
        return True
