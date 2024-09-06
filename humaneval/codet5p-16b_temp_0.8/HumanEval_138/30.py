
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = str(n)
    index = 0
    even_numbers = []
    while index < len(n):
        if int(n[index]) % 2 == 0:
            even_numbers.append(int(n[index]))
        index += 1
    index = 0
    while index < len(even_numbers):
        if int(n) - even_numbers[index] not in even_numbers:
            return False
        index += 1
    return True
