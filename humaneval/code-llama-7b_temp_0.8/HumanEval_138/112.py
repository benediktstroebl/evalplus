
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    even_numbers = []
    sum_of_even_numbers = 0
    while sum_of_even_numbers < n:
        even_numbers.append(sum_of_even_numbers)
        sum_of_even_numbers += 2
    if sum_of_even_numbers > n:
        even_numbers.pop()
    if len(even_numbers) == 4:
        return True
    return False
