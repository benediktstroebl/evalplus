def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result